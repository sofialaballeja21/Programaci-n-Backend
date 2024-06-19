from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Bratz
from .serializers import BratzSerializers
from .form import BratzForm  # Asegúrate de que este es el archivo correcto

def get_all_Bratz():
    bratz = Bratz.objects.all().order_by("name")
    bratz_serializers = BratzSerializers(bratz, many=True)
    return bratz_serializers.data

def bratz_rest(request):
    bratz = get_all_Bratz()
    return JsonResponse(bratz, safe=False)

def index_bratz(request):
    bratz = get_all_Bratz()
    print(bratz)
    return render(request, 'index_bratz.html', {'bratz': bratz})

class NewBratz(CreateView):
    form_class = BratzForm
    template_name = 'NewBratz.html'
    success_url = reverse_lazy('index_bratz')
    
def add_bratz(request):
    if request.method == 'POST':
        form = BratzForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_bratz')
    else:
        form = BratzForm()
    
    context = {
        'form': form,
    }
    return render(request, 'NewBratz.html', context)
