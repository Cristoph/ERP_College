from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  .models import Attorney



class HomeView(View):
    template = 'ModuleCommon/home.html'

    def get(self, request):


        return render(request, self.template, locals())


