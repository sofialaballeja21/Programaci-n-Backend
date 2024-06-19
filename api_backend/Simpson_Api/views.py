from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from Simpson_Api.models import Simpson
from Simpson_Api.serializers import SimpsonSerializer
from Simpson_Api.form import SimpsonForm
# Create your views here.

def get_all_simpson():
    simpsons = Simpson.objects.all().order_by("name")
    simpsons_serializers = SimpsonSerializer(simpsons, many = True)
    return simpsons_serializers.data

def simpson_rest(request):
    simpsons = get_all_simpson()
    return JsonResponse(simpsons, safe=False)

def index_simpson(request):
    simpsons = get_all_simpson()
    print(simpsons)
    return render(request,'index_simpson.html', {'simpson': simpsons})

class NewSimpson(CreateView):
    form_class = SimpsonForm
    template_name = 'NewSimpson.html'
    success_url = '/'