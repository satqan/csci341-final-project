from .views import DiseaseList, DiseaseCreate, DiseaseUpdate, DiseaseDetail, DiseaseDelete
from django.urls import path

urlpatterns = [
    path('', DiseaseList.as_view(), name='Disease_list'),
    path('view/<str:pk>', DiseaseDetail.as_view(), name='Disease_view'),
    path('new', DiseaseCreate.as_view(), name='Disease_new'),
    path('edit/<str:pk>', DiseaseUpdate.as_view(), name='Disease_edit'),
    path('delete/<str:pk>', DiseaseDelete.as_view(), name='Disease_delete'),
]
