from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ResidentialComplex, ResidentialPremise
from .serializers import (ResidentialComplexListSerializer, ResidentialComplexDetailSerializer,
                          ResidentialPremiseListSerializer, ResidentialPremiseDetailSerializer)


class ResidentialComplexListView(APIView):

    def get(self, request):
        premises = ResidentialComplex.objects.all() \
            .select_related('region', 'city', 'district', 'street', 'num_house', 'developer', 'class_of_housing') \
            .prefetch_related('deadline', 'metro_stations', 'infrastructure', 'material_walls', 'apart_decoration') \
            .prefetch_related('images_residential_complex', 'video_residential_complex')

        serializer = ResidentialComplexListSerializer(premises, many=True)
        return Response(serializer.data)


class ResidentialComplexDetailView(APIView):

    def get(self, request, pk):
        premises = ResidentialComplex.objects \
            .select_related('region', 'city', 'district', 'street', 'num_house', 'developer', 'class_of_housing') \
            .get(id=pk)

        serializer = ResidentialComplexDetailSerializer(premises)
        return Response(serializer.data)


class ResidentialPremiseListView(APIView):

    def get(self, request):
        premises = ResidentialPremise.objects.all() \
            .select_related('res_complex', 'number_rooms')\
            .prefetch_related('floor', 'floor_residential_premises')

        serializer = ResidentialPremiseListSerializer(premises, many=True)
        return Response(serializer.data)


class ResidentialPremiseDetailView(APIView):

    def get(self, request, pk):
        premises = ResidentialPremise.objects \
            .select_related('res_complex', 'number_rooms') \
            .get(id=pk)

        serializer = ResidentialPremiseDetailSerializer(premises)
        return Response(serializer.data)

