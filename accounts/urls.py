from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('api/u/<slug:user>/accounts/', views.UserAccountList.as_view(), name='user_accounts'),
]
