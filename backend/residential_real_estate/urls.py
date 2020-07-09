from django.urls import path, include

from .views import (ResidentialComplexListView, ResidentialComplexDetailView,
                    ResidentialPremiseListView, ResidentialPremiseDetailView)


urlpatterns = [
    path('complex/all/', ResidentialComplexListView.as_view()),
    path('complex/<int:pk>/', ResidentialComplexDetailView.as_view()),
    path('premises/all/', ResidentialPremiseListView.as_view()),
    path('premises/<int:pk>/', ResidentialPremiseDetailView.as_view()),
]
