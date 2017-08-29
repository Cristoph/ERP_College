from django.http import HttpResponse
from django.shortcuts import render
from django.views import View





class HomeView(View):
    template = 'ModuleCommon/home.html'

    def get(self, request):


        return render(request, self.template, locals())

# class AttorneyListView(ListView):
#     model = Attorney
#
#
#
#
# class AttorneyDetailView(DetailView):
#     model = Attorney
#     slug_field = 'rut'
#
#     def render_to_response(self, context, **response_kwargs):
#         return JsonResponse(json.dumps(list(context)), **response_kwargs)
#
# class StudentListView(Student):
#     model = Student
#
#
# class StudentDetailView(DetailView):
#     model = Student
#
#
# class TeacherListView(ListView):
#     model = Teacher
#
#
# class TeacherDetailView(DetailView):
#     model = Teacher
#
#
# class AdministrativeListView(ListView):
#     model = Administrative
#
#
# class AdministrativeDetailView(DetailView):
#     model = Administrative
