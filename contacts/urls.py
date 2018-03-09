from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('api/contact/', views.ContactCreate.as_view(), name='contact_create'),
    path('api/contact/list/account/<slug:account>/', views.ContactList.as_view(), name='contact_list'),
    path('api/address/', views.AddressCreate.as_view(), name='address_create'),
    path('api/address/<int:address>/', views.AddressRetrieve.as_view(), name='address_retrieve'),
]
