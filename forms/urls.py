from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('api/form/list/account/<slug:account>/', views.FormList.as_view(), name='list_create'),
    path('api/form/retrieve/<slug:form>/account/<slug:account>/', views.FormRetrieve.as_view(), name='retrieve_update_delete'),
    path('api/form/render/<slug:form>/account/<slug:account>/', views.FormRender.as_view(), name='render'),
]
