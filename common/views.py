from django.shortcuts import render
from django.views.generic.list import ListView
from common.models import student

# Create your views here.
class CommonList(ListView):
    model = student.objects.all()

def vist(request):
    model = student.objects.all()
    print(model)
    return render(request, 'index.html', model)
