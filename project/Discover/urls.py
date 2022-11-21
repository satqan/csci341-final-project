from .views import DiscoverList, DiscoverCreate, DiscoverUpdate, DiscoverDetail, DiscoverDelete
from django.urls import path

urlpatterns = [
    path('', DiscoverList.as_view(), name='Discover_list'),
    path('view/<str:pk>', DiscoverDetail.as_view(), name='Discover_view'),
    path('new', DiscoverCreate.as_view(), name='Discover_new'),
    path('edit/<str:pk>', DiscoverUpdate.as_view(), name='Discover_edit'),
    path('delete/<str:pk>', DiscoverDelete.as_view(), name='Discover_delete'),
]
