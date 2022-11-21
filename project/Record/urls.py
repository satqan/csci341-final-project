from .views import RecordList, RecordCreate, RecordUpdate, RecordDetail, RecordDelete
from django.urls import path

urlpatterns = [
    path('', RecordList.as_view(), name='Record_list'),
    path('view/<str:pk>', RecordDetail.as_view(), name='Record_view'),
    path('new', RecordCreate.as_view(), name='Record_new'),
    path('edit/<str:pk>', RecordUpdate.as_view(), name='Record_edit'),
    path('delete/<str:pk>', RecordDelete.as_view(), name='Record_delete'),
]
