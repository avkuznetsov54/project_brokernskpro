from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (BusinessCategory, TypeCommercialEstate, CookerHood, TypeEntranceToCommercialEstate,
                     CommunicationSystems, RelativeLocation, CommercialEstate, FinishingProperty, PurchaseMethod,
                     BusinessCenter, ImagesCommercialEstate, FloorPlansCommercialEstate, VideoCommercialEstate)


class ImagesCommercialPremisesInline(admin.TabularInline):
    model = ImagesCommercialEstate
    extra = 1
    readonly_fields = ('image_thumb', 'get_image_thumb',)

    def get_image_thumb(self, obj):
        return mark_safe(f'<img src={obj.image_thumb.url} height="70"')

    get_image_thumb.short_description = "Изображение"


class FloorPlansCommercialPremisesInline(admin.TabularInline):
    model = FloorPlansCommercialEstate
    extra = 1
    readonly_fields = ('image_thumb', 'get_image_thumb',)

    def get_image_thumb(self, obj):
        return mark_safe(f'<img src={obj.image_thumb.url} height="70"')

    get_image_thumb.short_description = "Изображение"


class VideoCommercialPremisesInline(admin.TabularInline):
    model = VideoCommercialEstate
    extra = 1


@admin.register(ImagesCommercialEstate)
class ImagesCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(FloorPlansCommercialEstate)
class FloorPlansCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(TypeCommercialEstate)
class TypeCommercialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CookerHood)
class CookerHoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(TypeEntranceToCommercialEstate)
class TypeEntranceToCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CommunicationSystems)
class CommunicationSystemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(RelativeLocation)
class RelativeLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(FinishingProperty)
class FinishingPropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(PurchaseMethod)
class PurchaseMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(BusinessCenter)
class BusinessCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CommercialEstate)
class CommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'district', 'area', 'is_sale', 'is_rent', 'is_active')
    list_display_links = ('address',)
    list_filter = ('is_active', 'is_sale', 'is_rent', 'district',)
    search_fields = ("address",)
    inlines = [ImagesCommercialPremisesInline, FloorPlansCommercialPremisesInline, VideoCommercialPremisesInline]
    save_on_top = True
    save_as = True
    list_editable = ("is_active",)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            'fields': (
                'is_active',
                'is_group_multiple_objs',
                ('is_sale', 'is_rent'),
            ),
        }),
        (None, {
            'fields': ('use_contacts_fixed_agent',
                       'fixed_agent',
                       # 'get_fixed_agent',
                       ),
        }),
        (None, {
            'fields': ('area',
                       'min_area',
                       'max_area',
                       'several_floors',
                       'ground_floor',
                       'basement',
                       'floor',
                       'number_of_storeys',
                       'region',
                       'city',
                       'district',
                       'address',
                       'distance_to_metro',
                       'metro_stations',
                       'relative_location',
                       'business_center',
                       'residential_complex',
                       'building_commercial_estate',
                       'finished_commercial_estate',
                       'type_commercial_estate',
                       'business_category',
                       'purchase_method',
                       ),
        }),
        (None, {
            'fields': (
                ('rent_price_sq_m', 'rent_price_month'),
                'cost_of_sale',
                ('min_cost_of_sale', 'max_cost_of_sale'),
                ('min_payback', 'max_payback'),
                ('min_average_rental_rate', 'max_average_rental_rate'),
                'possible_income',
            ),
        }),
        (None, {
            'fields': (
                'year_construction',
                'finishing_property',
                'kw',
                'min_kw',
                'max_kw',
                'comment_kw',
                'ceiling_height',
                'min_ceiling_height',
                'max_ceiling_height',
                'comment_ceiling_height',
                'communication_systems',
                'cooker_hood',
                'type_entrance',
                'parking',
                'min_parking',
                'max_parking',
                'comment_parking',
            ),
        }),
        (None, {
            'fields': ('description',
                       ),
        }),
        (None, {
            'fields': ('longitude',
                       'latitude',
                       ),
        }),
        (None, {
            'fields': (
                'main_image',
                'alt_attr',
                'main_image_thumb',
                'get_image',
            ),
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image_thumb.url} height="150"')

    get_image.short_description = ''

    # def get_fixed_agent(self, obj):
    #     return obj


@admin.register(VideoCommercialEstate)
class VideoCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_on_video', 'add_text')
    list_display_links = ('id',)


admin.site.site_title = "BROKERNSK.PRO"
admin.site.site_header = "BROKERNSK.PRO"
