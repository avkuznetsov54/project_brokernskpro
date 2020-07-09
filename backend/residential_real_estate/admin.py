from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Deadline, Developer, ClassOfHousing, FloorInBuilding,  ResidentialComplex,
                     ImagesResidentialComplex, FloorPlansResidentialPremise,
                     NamesOfMetroStations, MaterialWallsOfHouse, ApartmentDecoration, Infrastructure,
                     NumberOfRooms, ResidentialPremise, VideoResidentialComplex)


class ImagesResidentialComplexInline(admin.TabularInline):
    model = ImagesResidentialComplex
    extra = 1
    readonly_fields = ('image_thumb', 'get_image_thumb',)

    def get_image_thumb(self, obj):
        return mark_safe(f'<img src={obj.image_thumb.url} height="70"')

    get_image_thumb.short_description = "Изображение"


class FloorPlansResidentialPremiseInline(admin.TabularInline):
    model = FloorPlansResidentialPremise
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


class VideoResidentialComplexInline(admin.TabularInline):
    model = VideoResidentialComplex
    extra = 1


@admin.register(NumberOfRooms)
class NumberOfRoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'additional_name', 'description')
    list_display_links = ('name',)


@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_date', 'only_year', 'only_quarter')
    list_display_links = ('full_date',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ClassOfHousing)
class ClassNewBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ImagesResidentialComplex)
class ImagesResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)
    readonly_fields = ('image_thumb',)


@admin.register(FloorPlansResidentialPremise)
class FloorPlansResidentialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr', 'residential_premises')
    list_display_links = ('id',)


@admin.register(FloorInBuilding)
class FloorInBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_floor')
    list_display_links = ('num_floor',)


@admin.register(NamesOfMetroStations)
class NamesOfMetroStationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'distance_to_center')
    list_display_links = ('name',)


@admin.register(MaterialWallsOfHouse)
class MaterialWallsOfHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ApartmentDecoration)
class ApartmentDecorationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ResidentialComplex)
class ResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'developer', 'is_active')
    list_display_links = ('name',)
    list_filter = ('is_active', 'developer',)
    search_fields = ('name', 'developer',)
    readonly_fields = ('main_image_thumb',)
    inlines = [ImagesResidentialComplexInline, VideoResidentialComplexInline]
    save_on_top = True
    save_as = True
    list_editable = ("is_active",)


@admin.register(ResidentialPremise)
class ResidentialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_rooms', 'area', 'price', 'res_complex', 'is_active')
    list_display_links = ('id', 'number_rooms', )
    inlines = [FloorPlansResidentialPremiseInline]


@admin.register(VideoResidentialComplex)
class VideoResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_on_video', 'residential_complex')
    list_display_links = ('id',)


admin.site.site_title = "BROKERNSK.PRO"
admin.site.site_header = "BROKERNSK.PRO"

