from re import split

from django.http import HttpRequest
from django.shortcuts import render
from ModuleCommon.models import Qualification
from django.views import View
import  json
import requests
from ERP_College.settings import WEBService


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

class EnrollmentReport(View):
    template = 'ModuleReports/enrollment.html'

    def get(self, request, *args, **kwargs):
        print(kwargs['id'])

        enrollment = requests.get(WEBService + 'enrollment' + '/' + kwargs['id'])
        enrollment = enrollment.json()
        print(enrollment)
        student = requests.get(WEBService + 'student_id' + '/' + str(enrollment['student']))
        student = student.json()
        print(student)
        attorney = requests.get(WEBService + 'attorney_id' + '/' + str(student['attorney']))
        attorney = attorney.json()
        print(attorney)
        date = split('T', enrollment['created_at'])
        print(date[0])
        date = date[0]
        grade = requests.get(WEBService + 'grade' + '/' + str(enrollment['grade']))
        grade = grade.json()
        print(grade)
        return render(request, self.template, locals())