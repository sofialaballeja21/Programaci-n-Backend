from django.urls import path

from Bratz_Api import views
from .views import NewBratz, NewBratz,add_bratz

urlpatterns = [
   
    path('index_bratz', views.index_bratz, name='index_bratz.html'),
    path('bratz_rest/', views.bratz_rest, name ='bratz_rest'),
    path('new_bratz/', NewBratz.as_view(), name='new_bratz'),
     path('add_bratz/', add_bratz, name='add_bratz'),

]
