from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from  .forms import AttorneyForm
import  json
import requests

class AdminGrades(View):
    template = 'ModuleAdmin/grades.html'

    def get(self, request):
        return render(request, self.template, locals())



class AdminSubjects(View):
    template = 'ModuleAdmin/subjects.html'

    def get(self, request):
        return render(request, self.template, locals())



class AdminTeachers(View):
    template = 'ModuleAdmin/teachers.html'

    def get(self, request):
        return render(request, self.template, locals())



class AdminStudents(View):
    template = 'ModuleAdmin/students.html'

    def get(self, request):
        return render(request, self.template, locals())


class AdminAdmission(View):
    template = 'ModuleAdmin/admissionattorney.html'

    def get(self, request, *args, **kwargs):

        form = AttorneyForm()
        self.template = 'ModuleAdmin/admissionattorney.html'

        return render(request, self.template, locals())

    def post(self, request, **kwargs):

        form = AttorneyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.birthdate.day)
            set_data='{"rut":"'+obj.rut+'",' \
                    ' "first_name": "'+obj.first_name+'",' \
                    '"last_name": "'+obj.last_name+'",' \
                    '"gender": "'+obj.gender+'",' \
                    '"address": "'+obj.address+'",' \
                    '"email": "'+obj.email+'",' \
                    '"birthdate": "2007-09-26",' \
                    '"age": 17,' \
                    '"phone": 12345,' \
                    '"cellphone": 12345}'

            set_data=json.loads(set_data)
            requests.post('http://127.0.0.1:8888/api/attorney/', data=set_data)
            #form.save()
            return redirect('module_admin:admission_student', pk=obj.rut)
        else:
            print(form.is_valid())
            print(form.errors)
            form = AttorneyForm(request.POST)
        return render(request, self.template, locals())

class AdminAdmissionStudent(View):
    template = 'ModuleAdmin/admissionstudents.html'

    def get(self, request, *args, **kwargs):
        print(kwargs['pk'])
        self.template = 'ModuleAdmin/admissionstudents.html'

        return render(request, self.template, locals())

