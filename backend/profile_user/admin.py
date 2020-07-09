from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe

from .models import Specialization, SocialNetwork, JobTitle
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 1


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'full_name', 'phone_number', 'get_specialization', 'is_staff', 'is_active')
    list_display_links = ('id', 'email', 'full_name',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'specialization', )
    search_fields = ('email', 'full_name', 'phone_number',)
    save_on_top = True
    list_editable = ("is_active",)
    readonly_fields = ('update_date', 'get_image_thumb')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None,
         {'fields':
             (
                 'full_name', 'email', 'password', 'phone_number', 'specialization', 'job_title', 'gender',
                 'birth_date', 'bio', 'image', 'image_thumb', 'get_image_thumb'
             )
         }
         ),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (None, {'fields': ('date_joined', 'update_date', 'last_login')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    def get_image_thumb(self, obj):
        return mark_safe(f'<img src={obj.image_thumb.url} height="200"')

    get_image_thumb.short_description = "Изображение"

    def get_specialization(self, obj):
        s = obj.specialization
        return "\n".join([p.short_name for p in s.all()])

    get_specialization.short_description = 'Специализация'


admin.site.register(User, UserAdmin)

admin.site.site_title = "BROKERNSK.PRO"
admin.site.site_header = "BROKERNSK.PRO"


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name')
    list_display_links = ('id', 'name',)


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name')
    list_display_links = ('id', 'name',)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'link_on_socnet')
    list_display_links = ('id', 'name',)
