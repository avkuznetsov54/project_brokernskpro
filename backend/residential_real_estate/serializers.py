from rest_framework import serializers

from .models import (ResidentialComplex, ResidentialPremise, ImagesResidentialComplex,
                     FloorPlansResidentialPremise, VideoResidentialComplex)


class ImagesResidentialComplexListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesResidentialComplex
        fields = '__all__'


class VideoResidentialComplexListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoResidentialComplex
        fields = '__all__'


class FloorPlansResidentialPremiseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlansResidentialPremise
        fields = '__all__'


class ResidentialComplexListSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    developer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class_of_housing = serializers.SlugRelatedField(slug_field='name', read_only=True)

    address = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    deadline = serializers.SlugRelatedField(slug_field='full_date', read_only=True, many=True)
    metro_stations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    infrastructure = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    material_walls = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    apart_decoration = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_residential_complex = ImagesResidentialComplexListSerializer(many=True, read_only=True)
    video_residential_complex = VideoResidentialComplexListSerializer(many=True, read_only=True)

    class Meta:
        model = ResidentialComplex
        fields = '__all__'


class ResidentialComplexDetailSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    developer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class_of_housing = serializers.SlugRelatedField(slug_field='name', read_only=True)

    address = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    deadline = serializers.SlugRelatedField(slug_field='full_date', read_only=True, many=True)
    metro_stations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    infrastructure = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    material_walls = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    apart_decoration = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_residential_complex = ImagesResidentialComplexListSerializer(many=True, read_only=True)
    video_residential_complex = VideoResidentialComplexListSerializer(many=True, read_only=True)

    class Meta:
        model = ResidentialComplex
        fields = '__all__'


class ResidentialPremiseListSerializer(serializers.ModelSerializer):
    res_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)
    number_rooms = serializers.SlugRelatedField(slug_field='name', read_only=True)

    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)

    floor_residential_premises = FloorPlansResidentialPremiseListSerializer(many=True, read_only=True)

    class Meta:
        model = ResidentialPremise
        fields = '__all__'


class ResidentialPremiseDetailSerializer(serializers.ModelSerializer):
    res_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)
    number_rooms = serializers.SlugRelatedField(slug_field='name', read_only=True)

    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)

    floor_residential_premises = FloorPlansResidentialPremiseListSerializer(many=True, read_only=True)

    class Meta:
        model = ResidentialPremise
        fields = '__all__'
