from django.urls import path

from . import views

app_name = 'emails'
urlpatterns = [
    path('api/emails/list/account/<slug:account>/', views.EmailCampaignList.as_view(), name='list_create'),
    path('api/emails/retrieve/<slug:cmid>/account/<slug:account>/', views.EmailCampaignRetrieve.as_view(),
         name='retrieve'),
]
