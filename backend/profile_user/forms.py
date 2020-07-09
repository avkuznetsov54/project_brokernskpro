from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()


# class UserAdminCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
#     password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('full_name', 'email',) #'full_name',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserAdminCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('full_name', 'email',)


#
# class UserDetailChangeForm(forms.ModelForm):
#     full_name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['full_name']


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'is_active', 'is_superuser', 'groups')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
