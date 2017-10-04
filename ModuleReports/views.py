from re import split

from django.http import HttpRequest
from django.shortcuts import render
from ModuleCommon.models import Qualification
from django.views import View
import  json
import requests
from decimal import Decimal
from ERP_College.settings import WEBService


class ReportQualifications(View):
    template = 'ModuleReports/report-qualifications.html'

    def get(self, request, *args, **kwargs):

        subject = requests.get(WEBService + 'subject')
        subject = subject.json()
        quali = requests.get(WEBService+'quali_id/'+kwargs['id']+'/')
        quali = quali.json()
        student = requests.get(WEBService+'student_id/'+kwargs['id']+'/')
        student = student.json()
        enrollment = requests.get(WEBService+'enrollment_st/'+kwargs['id']+'/')
        enrollment = enrollment.json()
        grade = requests.get(WEBService+'grade/'+str(enrollment['grade'])+'/')
        grade = grade.json()
        teacher = requests.get(WEBService+'teacher_id/'+str(grade['teacher'])+'/')
        teacher = teacher.json()
        for qua in quali:
            print(qua)
        quali_ = []
        qualis = []
        i = 0
        for ll in subject:
            quali_ =[{'id': ll['id'],
                      'name': ll['name'],
                         'ps': '',
                         'pf': '',
                         }]


            o = 0

            while o < 10:
                o += 1
                quali_[i][o] = ''

            for qua in quali:
                if qua['teacher_subject'] == ll['id']:
                    quali_[i][qua['position']] = qua['value']

            o = 0
            sm = 0
            pm = 0
            while o < 10:
                o += 1
                if quali_[i][o] != '':
                    sm += Decimal(quali_[i][o])
                    pm += 1
            if pm != 0:
                quali_[i]['ps'] = round(float(sm / pm), 1)
                quali_[i]['pf'] = round(float(sm / pm), 1)

            #i += 1
            print('i ='+str(i))
            qualis+=quali_
        i=0
        su=0
        for lk in qualis:
            if lk['ps']!='':
                su+= Decimal(lk['ps'])
                i+=1
            print(lk)
        su= round(float(su / i), 1)
        print(su)
        return render(request, self.template, locals())



class EnrollmentReport(View):
    template = 'ModuleReports/enrollment.html'

    def get(self, request, *args, **kwargs):
        print(kwargs['id'])

        enrollment = requests.get(WEBService + 'enrollment' + '/' + kwargs['id'])
        enrollment = enrollment.json()
        student = requests.get(WEBService + 'student_id' + '/' + str(enrollment['student']))
        student = student.json()
        attorney = requests.get(WEBService + 'attorney_id' + '/' + str(student['attorney']))
        attorney = attorney.json()
        date = split('T', enrollment['created_at'])
        date = date[0]
        grade = requests.get(WEBService + 'grade' + '/' + str(enrollment['grade']))
        return render(request, self.template, locals())