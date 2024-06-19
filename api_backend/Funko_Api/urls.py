from django.urls import path
from Funko_Api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
   
    path('index_funkos', views.index, name='index_funkos'),
   
    # path('add_funko/', views.add_funko_view, name='add_funko'),
    path('new_funko/', views.NewFunkoView.as_view(), name='new_funko'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
    
]