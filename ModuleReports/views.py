from django.http import HttpRequest
from django.shortcuts import render
from ModuleCommon.models import Qualification
from django.views import View
import  json
import requests
class ReportQualifications(View):
    template = 'ModuleReports/report-qualifications.html'

    def get(self, request, *args, **kwargs):
        r = requests.get('http://127.0.0.1:8888/api/quali/'+kwargs['pk']+'/')
        json = r.json()
        qualifications= json
        for quali in json:
            print(quali['teacher_subject'])

        data = {
            'qualifications': qualifications,
                }
        return render(request, self.template, locals(), data)