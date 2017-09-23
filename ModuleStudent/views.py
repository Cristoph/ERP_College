from django.shortcuts import render
from django.views import View


class StudentQualifications(View):
    template = 'ModuleStudent/qualifications.html'

    def get(self, request):

        return render(request, self.template, locals())

