from .views import SpecializeList, SpecializeCreate, SpecializeUpdate, SpecializeDetail, SpecializeDelete
from django.urls import path

urlpatterns = [
    path('', SpecializeList.as_view(), name='Specialize_list'),
    path('view/<str:pk>', SpecializeDetail.as_view(), name='Specialize_view'),
    path('new', SpecializeCreate.as_view(), name='Specialize_new'),
    path('edit/<str:pk>', SpecializeUpdate.as_view(), name='Specialize_edit'),
    path('delete/<str:pk>', SpecializeDelete.as_view(), name='Specialize_delete'),
]
