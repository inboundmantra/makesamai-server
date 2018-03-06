from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('api/a/<slug:account>/contact/', views.ContactList.as_view(), name='contact_list'),
    path('api/address/<int:address>/', views.AddressDetail.as_view(), name='address_detail'),
]
