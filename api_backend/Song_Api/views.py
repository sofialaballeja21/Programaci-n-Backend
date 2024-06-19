from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from Song_Api.models import Song
from Song_Api.serializers import SongSerializers
from Song_Api.form import SongForm


# Create your views here.

def get_all_song():
    song = Song.objects.all().order_by('name_song')
    song_serializers = SongSerializers(song, many=True)
    return song_serializers.data

def index_song(request):
    song = get_all_song()
    return render(request,'index_song.html', {'song':song})

def song_rest(request):
    song = get_all_song()
    return JsonResponse(song, safe=False)


class NewSong(CreateView):
    form_class = SongForm
    template_name = 'NewSong.html'
    success_url = '/'