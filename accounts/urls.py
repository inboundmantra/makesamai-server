from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('api/account/create/', views.AccountCreate.as_view(), name='create'),
    path('api/account/u/<slug:user>/', views.UserAccountList.as_view(), name='list'),
    path('api/account/<slug:uaid>/', views.AccountRetrieve.as_view(), name='retrieve'),
]
