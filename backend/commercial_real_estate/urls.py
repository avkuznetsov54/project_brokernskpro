from django.urls import path, include

from .views import CommercialEstateListView, CommercialEstateDetailView


urlpatterns = [

    path('all/', CommercialEstateListView.as_view()),
    path('<int:pk>/', CommercialEstateDetailView.as_view()),
]
