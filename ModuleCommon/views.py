from django.shortcuts import render
from django.views.generic.list import ListView
from ModuleCommon.models import Student

# Create your views here.
class CommonList(ListView):
    model = Student.objects.all()

def vist(request):
    model = Student.objects.all()
    print(model)
    return render(request, 'index.html', model)
