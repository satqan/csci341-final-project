from .views import PublicServantList, PublicServantCreate, PublicServantUpdate, PublicServantDetail, PublicServantDelete
from django.urls import path

urlpatterns = [
    path('', PublicServantList.as_view(), name='PublicServant_list'),
    path('view/<str:pk>', PublicServantDetail.as_view(), name='PublicServant_view'),
    path('new', PublicServantCreate.as_view(), name='PublicServant_new'),
    path('edit/<str:pk>', PublicServantUpdate.as_view(), name='PublicServant_edit'),
    path('delete/<str:pk>', PublicServantDelete.as_view(), name='PublicServant_delete'),
]
