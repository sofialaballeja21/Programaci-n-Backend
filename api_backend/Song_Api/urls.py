from Song_Api import views
from django.urls import path
from .views import NewSong

urlpatterns = [
    path('index_song', views.index_song, name='index_song'),
    path('song_rest', views.song_rest, name='song_rest'),
    path('new_song/', NewSong.as_view(), name='new_song'),
]