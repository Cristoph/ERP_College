from django.shortcuts import render
from django.views import View


class TeacherSchedules(View):
    template = 'ModuleTeacher/schedules.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherQualifications(View):
    template = 'ModuleTeacher/qualifications.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherAssistances(View):
    template = 'ModuleTeacher/assistances.html'

    def get(self, request):
        return render(request, self.template, locals())



class TeacherAnnotations(View):
    template = 'ModuleTeacher/annotations.html'

    def get(self, request):
        return render(request, self.template, locals())


