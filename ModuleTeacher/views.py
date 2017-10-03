from django.shortcuts import render
from django.views import View
from decimal import Decimal
import requests
from ERP_College.settings import WEBService

class TeacherSchedules(View):
    template = 'ModuleTeacher/schedules.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherQualifications(View):
    template = 'ModuleTeacher/qualifications.html'

    def get(self, request):
        subject = requests.get(WEBService + 'subject')
        subject = subject.json()
        grade = requests.get(WEBService + 'grade')
        grade = grade.json()
        return render(request, self.template, locals())

class TeacherQualificationsSet(View):
    template = 'ModuleTeacher/qualifications.html'


    def get(self, request, *args, **kwargs):

        subject = requests.get(WEBService + 'subject')
        subject = subject.json()
        grade = requests.get(WEBService + 'grade')
        grade = grade.json()
        for on in grade:
            if int(on['id']) == int(kwargs['grade']):
                grade_= on
        for on in subject:
            if int(on['id']) == int(kwargs['subject']):
                subject_= on
        teacher_subject = requests.get(WEBService + 'teacher_subject_sub/'+kwargs['subject'])

        if str(teacher_subject) != '<Response [500]>':
            teacher_subject = teacher_subject.json()
        student_ = requests.get(WEBService + 'student_list_grade/' + kwargs['grade'])
        student_= student_.json()

        quali = requests.get(WEBService + 'quali_grade/' + kwargs['grade']+'/'+kwargs['subject'])
        quali=quali.json()

        student = self.studentQuialificatuions(student_, quali)
        return render(request, self.template, locals())

    def studentQuialificatuions(self, student_, quali):
        student=[]
        i=0
        for ll in student_:
            student+=[{'id':ll['id'],
                        'rut':ll['rut'],
                       'name':ll['first_name']+' '+ll['last_name'],
                       'ps':'',
                       'pf':'',
                       }]
            o=0
            while o <10:
                o+=1
                student[i][o] = ''
            for qua in quali:
                if qua['student']==ll['id']:
                    student[i][qua['position']]=qua['value']
            o = 0
            sm = 0
            pm = 0
            while o < 10:
                o += 1
                if student[i][o]!= '':
                    sm+=Decimal(student[i][o])
                    pm+=1
            if pm != 0:
                student[i]['ps']=round(float(sm/pm), 1)
            i+=1
        return student



class TeacherAssistances(View):
    template = 'ModuleTeacher/assistances.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherAnnotations(View):
    template = 'ModuleTeacher/annotations.html'

    def get(self, request):
        return render(request, self.template, locals())


