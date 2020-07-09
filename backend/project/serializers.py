from rest_framework import serializers

from geo_location.models import City, District, Street
from residential_real_estate.models import NamesOfMetroStations, ResidentialComplex, ClassOfHousing
from commercial_real_estate.models import (TypeCommercialEstate, BusinessCategory, RelativeLocation, FinishingProperty,
                                           CommunicationSystems, CookerHood, TypeEntranceToCommercialEstate,
                                           PurchaseMethod, CommercialEstate, BusinessCenter)


class DistrictListSerializer(serializers.ModelSerializer):
    # city = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ('id', 'name')

    # def get_city(self, obj):
    #     return obj.city.name


class CityListSerializer(serializers.ModelSerializer):
    district_city = DistrictListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'district_city')


class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'name')


class TypeCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCommercialEstate
        fields = ('id', 'name')


class BusinessCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ('id', 'name')


class RelativeLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeLocation
        fields = ('id', 'name')


class NamesOfMetroStationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamesOfMetroStations
        fields = ('id', 'name')


class FinishingPropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishingProperty
        fields = ('id', 'name')


class CommunicationSystemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationSystems
        fields = ('id', 'name')


class CookerHoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookerHood
        fields = ('id', 'name')


class TypeEntranceToCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEntranceToCommercialEstate
        fields = ('id', 'name')


class ResidentialComplexListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialComplex
        fields = ('id', 'name')


class ClassOfHousingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassOfHousing
        fields = ('id', 'name')


class PurchaseMethodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseMethod
        fields = ('id', 'name')


class BusinessCenterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCenter
        fields = ('id', 'name')


class FiltersSerializers(serializers.Serializer):
    city = CityListSerializer(read_only=True, many=True)
    district = DistrictListSerializer(read_only=True, many=True)
    street = StreetListSerializer(read_only=True, many=True)
    type_commercial_estate = TypeCommercialEstateListSerializer(read_only=True, many=True)
    business_category = BusinessCategoryListSerializer(read_only=True, many=True)
    relative_location = RelativeLocationListSerializer(read_only=True, many=True)
    metro_stations = NamesOfMetroStationsListSerializer(read_only=True, many=True)
    finishing_property = FinishingPropertyListSerializer(read_only=True, many=True)
    communication_systems = CommunicationSystemsListSerializer(read_only=True, many=True)
    cooker_hood = CookerHoodListSerializer(read_only=True, many=True)
    type_entrance = TypeEntranceToCommercialEstateListSerializer(read_only=True, many=True)
    residential_complex = ResidentialComplexListSerializer(read_only=True, many=True)
    class_of_housing = ClassOfHousingListSerializer(read_only=True, many=True)
    purchase_method = PurchaseMethodListSerializer(read_only=True, many=True)
    business_center = BusinessCenterListSerializer(read_only=True, many=True)


class CountSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    class Meta:
        model = CommercialEstate
        fields = ('count', )

    def get_count(self, obj):
        return obj.count.count()
