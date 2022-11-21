from .views import CountryList, CountryCreate, CountryUpdate, CountryDetail, CountryDelete
from django.urls import path

urlpatterns = [
    path('', CountryList.as_view(), name='Country_list'),
    path('view/<str:pk>', CountryDetail.as_view(), name='Country_view'),
    path('new', CountryCreate.as_view(), name='Country_new'),
    path('edit/<str:pk>', CountryUpdate.as_view(), name='Country_edit'),
    path('delete/<str:pk>', CountryDelete.as_view(), name='Country_delete'),
]
