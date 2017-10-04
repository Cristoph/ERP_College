from django.shortcuts import render
from django.views import View
from decimal import Decimal
from django.shortcuts import redirect
import  json, requests
from ERP_College.settings import WEBService
from .forms import TransForm
import string

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
        teacher_subject = requests.get(WEBService + 'teacher_subject_sub/'+kwargs['subject'])
        if str(teacher_subject) != '<Response [500]>':
            teacher_subject = teacher_subject.json()
        edit = False
        form = None
        if kwargs['edit']=='True':
            edit=True
            form = TransForm()
            #print(form)
        for on in grade:
            if int(on['id']) == int(kwargs['grade']):
                grade_= on
        for on in subject:
            if int(on['id']) == int(kwargs['subject']):
                subject_= on
        student_ = requests.get(WEBService + 'student_list_grade/' + kwargs['grade'])
        student_= student_.json()
        quali = requests.get(WEBService + 'quali_grade/' + kwargs['grade']+'/'+kwargs['subject'])
        quali=quali.json()

        selgrade = int(kwargs['grade'])
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

    def post(self, request, **kwargs):
        form = TransForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            resive = obj.obj1.replace('-', '"')
            print(resive)
            quali = resive.split('&')
            for ll in quali:
                lo = ll.split('!')
                for ls in lo:
                    if ls == "":
                        print('sii')
                    else:
                        #print(ls)
                        ls = json.loads(ls)
                        if ls['value'] !='':
                            #print(ls)

                            resq = requests.get(WEBService + 'quali_detail/'
                                                  +str(ls['student'])+'/'
                                                  +str(ls['teacher_subject'])+'/'
                                                  +str(ls['position'])+'/')
                            resq = resq.json()
                            print(resq)
                            if resq != {'detail': 'Not found.'}:
                                resq=requests.put(WEBService + 'quali_detail/'
                                                  +str(ls['student'])+'/'
                                                  +str(ls['teacher_subject'])+'/'
                                                  +str(ls['position'])+'/', ls)
                                print(resq)
                            else:
                                resq = requests.post(WEBService + 'quali_detail/'
                                                    + str(ls['student']) + '/'
                                                    + str(ls['teacher_subject']) + '/'
                                                    + str(ls['position']) + '/', ls)
                                print(resq)
            return redirect('module_teacher:qualifications_set',
                            grade=kwargs['grade'],
                            subject=kwargs['subject'],
                            edit='False')
        return render(request, self.template, locals())



class TeacherAssistances(View):
    template = 'ModuleTeacher/assistances.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherAnnotations(View):
    template = 'ModuleTeacher/annotations.html'

    def get(self, request):
        return render(request, self.template, locals())


