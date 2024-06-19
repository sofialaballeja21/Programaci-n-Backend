from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from Funko_Api.form import FunkoForm, UserForm

from Funko_Api.models import Funko
from Funko_Api.serialarzers import FunkoSerializer
from django.middleware.csrf import get_token
# Create your views here.


def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data

def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)

def users_rest(reqest):
    #fnkos = get_all_funkos()
    return JsonResponse("Ok", safe=False)


class NewFunkoView(CreateView):
    form_class = FunkoForm
    template_name = 'form_funko.html'
    success_url = '/index_funkos/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_funko.html'
    success_url = '/'
