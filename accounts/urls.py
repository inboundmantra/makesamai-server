from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('api/accounts/u/<slug:user>/', views.UserAccountList.as_view(), name='user_accounts'),
]
