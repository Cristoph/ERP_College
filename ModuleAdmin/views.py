from django.shortcuts import render
from django.views import View


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
    template = 'ModuleAdmin/admissionstudents.html'

    def get(self, request, *args, **kwargs):
        if kwargs['value']=='students':
            self.template = 'ModuleAdmin/admissionstudents.html'

        if kwargs['value']=='attorney':
            self.template = 'ModuleAdmin/admissionattorney.html'

        if kwargs['value']=='enrollment':
            self.template = 'ModuleAdmin/admissionenrollment.html'

        return render(request, self.template, locals())

