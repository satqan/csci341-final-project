from .views import DoctorList, DoctorCreate, DoctorUpdate, DoctorDetail, DoctorDelete
from django.urls import path

urlpatterns = [
    path('', DoctorList.as_view(), name='Doctor_list'),
    path('view/<str:pk>', DoctorDetail.as_view(), name='Doctor_view'),
    path('new', DoctorCreate.as_view(), name='Doctor_new'),
    path('edit/<str:pk>', DoctorUpdate.as_view(), name='Doctor_edit'),
    path('delete/<str:pk>', DoctorDelete.as_view(), name='Doctor_delete'),
]
