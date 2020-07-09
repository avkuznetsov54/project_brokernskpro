from rest_framework import serializers

from .models import (CommercialEstate,
                     VideoCommercialEstate, ImagesCommercialEstate, FloorPlansCommercialEstate)
from profile_user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'phone_number', 'image_thumb')


class ImagesCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesCommercialEstate
        fields = '__all__'


class FloorPlansCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlansCommercialEstate
        fields = '__all__'


class VideoCommercialEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCommercialEstate
        fields = '__all__'


class CommercialEstateListSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)
    num_house = serializers.SlugRelatedField(slug_field='name', read_only=True)
    business_center = serializers.SlugRelatedField(slug_field='name', read_only=True)
    residential_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)

    cooker_hood = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    # скорее всего в fixed_agent нужен будет только id
    fixed_agent = serializers.SlugRelatedField(slug_field='full_name', read_only=True, many=True)
    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)
    relative_location = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_commercial_estate = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    business_category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    communication_systems = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_entrance = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    finishing_property = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    metro_stations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    purchase_method = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_commercial_estate = ImagesCommercialEstateListSerializer(many=True, read_only=True)
    floorplans_commercial_estate = FloorPlansCommercialEstateListSerializer(many=True, read_only=True)
    video_commercial_estate = VideoCommercialEstateListSerializer(many=True, read_only=True)

    class Meta:
        model = CommercialEstate
        fields = '__all__'


class CommercialEstateDetailSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)
    num_house = serializers.SlugRelatedField(slug_field='name', read_only=True)
    business_center = serializers.SlugRelatedField(slug_field='name', read_only=True)
    residential_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)

    cooker_hood = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    # скорее всего в fixed_agent нужен будет только id
    fixed_agent = serializers.SlugRelatedField(slug_field='full_name', read_only=True, many=True)
    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)
    relative_location = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_commercial_estate = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    business_category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    communication_systems = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_entrance = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    finishing_property = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    metro_stations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    purchase_method = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_commercial_estate = ImagesCommercialEstateListSerializer(many=True, read_only=True)
    floorplans_commercial_estate = FloorPlansCommercialEstateListSerializer(many=True, read_only=True)
    video_commercial_estate = VideoCommercialEstateListSerializer(many=True, read_only=True)

    # включаем данные из связанных моделей
    user = UserSerializer(source='fixed_agent', read_only=True, many=True)

    class Meta:
        model = CommercialEstate
        # exclude = ('is_active',)  # исключает поля
        fields = '__all__'

