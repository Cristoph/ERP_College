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

