from django.urls import path

from Simpson_Api import views
from .views import NewSimpson


urlpatterns = [
   
    path('index_simpson', views.index_simpson, name='index_simpson'),
    path('simpson_rest/', views.simpson_rest, name ='simpson_rest'),
    path('new_simpson/', NewSimpson.as_view(), name='new_simpson'), 
]