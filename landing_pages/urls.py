from django.urls import path

from . import views

app_name = 'landing_pages'
urlpatterns = [
    path('api/landing_page/list/account/<slug:account>/', views.LandingPageList.as_view(), name='list_create'),
    path('api/landing_page/retrieve/<slug:ulid>/account/<slug:account>/', views.LandingPageRetrieve.as_view(),
         name='retrieve_update_delete'),
    path('api/landing_page/render/<slug:ulid>/account/<slug:account>/', views.LandingPageRender.as_view(),
         name='render'),
]
