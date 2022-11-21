from .views import UsersList, UsersCreate, UsersUpdate, UsersDetail, UsersDelete
from django.urls import path

urlpatterns = [
    path('', UsersList.as_view(), name='Users_list'),
    path('view/<str:pk>', UsersDetail.as_view(), name='Users_view'),
    path('new', UsersCreate.as_view(), name='Users_new'),
    path('edit/<str:pk>', UsersUpdate.as_view(), name='Users_edit'),
    path('delete/<str:pk>', UsersDelete.as_view(), name='Users_delete'),
]
