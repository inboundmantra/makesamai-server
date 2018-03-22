from django.urls import path

from . import views

app_name = 'clients'
urlpatterns = [
    path('api/signup/', views.CreateClient.as_view(), name='create'),
    path('api/me/', views.UserView.as_view(), name='me'),
]
