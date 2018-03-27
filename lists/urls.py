from django.urls import path

from . import views

app_name = 'lists'
urlpatterns = [
    path('api/list/list/account/<slug:account>/', views.ListList.as_view(), name='list_create'),
    path('api/list/retrieve/<slug:list>/account/<slug:account>/', views.ListRetrieve.as_view(),
         name='retrieve_update_delete'),
]
