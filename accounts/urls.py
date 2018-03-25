from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('api/account/', views.UserAccountList.as_view(), name='list_create'),
    path('api/account/<slug:uaid>/', views.AccountRetrieve.as_view(), name='retrieve'),
]
