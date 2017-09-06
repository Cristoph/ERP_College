from django.shortcuts import render

from django.views import View




class ReportQualifications(View):
    template = 'ModuleReports/report-qualifications.html'

    def get(self, request):


        return render(request, self.template, locals())

