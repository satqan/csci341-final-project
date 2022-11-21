from .views import DiseaseTypeList, DiseaseTypeCreate, DiseaseTypeUpdate, DiseaseTypeDetail, DiseaseTypeDelete
from django.urls import path

urlpatterns = [
    path('', DiseaseTypeList.as_view(), name='DiseaseType_list'),
    path('view/<int:pk>', DiseaseTypeDetail.as_view(), name='DiseaseType_view'),
    path('new', DiseaseTypeCreate.as_view(), name='DiseaseType_new'),
    path('edit/<int:pk>', DiseaseTypeUpdate.as_view(), name='DiseaseType_edit'),
    path('delete/<int:pk>', DiseaseTypeDelete.as_view(), name='DiseaseType_delete'),
]
