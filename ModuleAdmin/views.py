from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from  .forms import AttorneyForm, RutForm, EnrollmentForm
from django.utils import timezone
import  json, requests
from ERP_College.settings import WEBService

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
    select = 'student/'
    def get(self, request):
        list = requests.get(WEBService+self.select)
        data = list.json()
        print(data)
        return render(request, self.template, locals())

class AdminAdmissionAttorney(View):
    template = 'ModuleAdmin/admissionattorney.html'

    def get(self, request, *args, **kwargs):
        form = RutForm()
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
                    '"age": '+str(obj.age)+',' \
                    '"phone": '+str(obj.phone)+',' \
                    '"cellphone": '+str(obj.cellphone)+'}'

            set_data=json.loads(set_data)
            requests.post(WEBService+'attorney/', data=set_data)
            #form.save()
            return redirect('module_admin:admission_student', pk=obj.rut)
        else:
            print(form.is_valid())
            print(form.errors)
            form = AttorneyForm(request.POST)
        return render(request, self.template, locals())

class AdminAdmissionAttorneySet(View):
    template = 'ModuleAdmin/admissionattorney.html'
    def get(self, request, *args, **kwargs):
        rut = kwargs['rut']
        print(rut)
        atto = requests.get(WEBService+'attorney/'+rut)
        atto = atto.json()
        print(atto)
        if atto != {'detail': 'Not found.'}:
            data ={'rut': atto['rut'],
                    'first_name' : atto['first_name'],
                    'last_name' : atto['last_name'],
                    'email': atto['email'],
                    'birthdate': atto['birthdate'],
                    'gender' : atto['gender'],
                    'address': atto['address'],
                    'phone': atto['phone'],
                    'cellphone' : atto['cellphone'],
                    'age': atto['age'],
                   }
            print(data)
        form = AttorneyForm()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        rut = kwargs['rut']
        form = AttorneyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.birthdate.year)
            print(timezone.now().year)
            age=timezone.now().year - obj.birthdate.year
            print(age)
            date=str(obj.birthdate)
            set_data='{"rut":"'+obj.rut+'",' \
                    ' "first_name": "'+obj.first_name+'",' \
                    '"last_name": "'+obj.last_name+'",' \
                    '"gender": "'+obj.gender+'",' \
                    '"address": "'+obj.address+'",' \
                    '"email": "'+obj.email+'",' \
                    '"birthdate": "'+date+'",' \
                    '"age": '+str(age)+',' \
                    '"phone": '+str(obj.phone)+',' \
                    '"cellphone": '+str(obj.cellphone)+'}'

            set_data=json.loads(set_data)

            ll = requests.post(WEBService+'attorney/'+obj.rut+'/', data=set_data)
            print(ll.json())
            if ll.json()['rut'] == ['attorney with this rut already exists.']:
                ll = requests.put(WEBService+'attorney/'+obj.rut+'/', data=set_data)
                print(ll.json())
            return redirect('module_admin:admission_student', rut=rut)
        else:
            print(form.is_valid())
            print(form.errors)
            form = AttorneyForm(request.POST)
        return render(request, self.template, locals())

class AdminAdmissionStudent(View):
    template = 'ModuleAdmin/admissionstudents.html'

    def get(self, request, *args, **kwargs):
        rut_a = kwargs['rut']
        form = RutForm()
        return render(request, self.template, locals())

class AdminAdmissionStudentSet(View):
    template = 'ModuleAdmin/admissionstudents.html'
    select = 'student'
    def get(self, request, *args, **kwargs):
        rut_a = kwargs['rut']
        rut_s= kwargs['student']
        print(rut_a+' - '+rut_s+' -> '+WEBService+self.select+'/'+rut_s)
        atto = requests.get(WEBService+self.select+'/'+rut_s)
        atto = atto.json()
        print(atto)
        if atto != {'detail': 'Not found.'}:
            """
            data ={'rut': atto['rut'],
                    'first_name' : atto['first_name'],
                    'last_name' : atto['last_name'],
                    'email': atto['email'],
                    'birthdate': atto['birthdate'],
                    'gender' : atto['gender'],
                    'address': atto['address'],
                    'phone': atto['phone'],
                    'cellphone' : atto['cellphone'],
                    'age': atto['age'],
                    'attorney' : atto['attorney']
                   } """
            data=atto
            print(data)
        form = AttorneyForm()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        rut = kwargs['rut']
        student= kwargs['student']
        form = AttorneyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            age=timezone.now().year - obj.birthdate.year
            attorney=1
            grade=1
            date=str(obj.birthdate)
            set_data='{"rut":"'+obj.rut+'",' \
                    ' "first_name": "'+obj.first_name+'",' \
                    '"last_name": "'+obj.last_name+'",' \
                    '"gender": "'+obj.gender+'",' \
                    '"address": "'+obj.address+'",' \
                    '"email": "'+obj.email+'",' \
                    '"birthdate": "'+date+'",' \
                    '"age": '+str(age)+',' \
                    '"phone": '+str(obj.phone)+',' \
                    '"cellphone": '+str(obj.cellphone)+','\
                    '"attorney": '+str(attorney)+','\
                    '"grade": '+str(grade)+'}'
            print(set_data)
            set_data=json.loads(set_data)
            ll = requests.post(WEBService+self.select+'/'+student+'/', data=set_data)
            print(WEBService+self.select+'/'+student+'/')
            print(ll.json())
            if ll.json()['rut'] == ['student with this rut already exists.']:
                ll = requests.put(WEBService+self.select+'/'+student+'/', data=set_data)
                print(ll.json())
            return redirect('module_admin:admission_enrollment_set', rut=rut, student=student)
        else:
            print(form.is_valid())
            print(form.errors)
            form = AttorneyForm(request.POST)
        return render(request, self.template, locals())

class AdminAdmissionenRollment(View):
    template = 'ModuleAdmin/admissionenrollment.html'

    def get(self, request, *args, **kwargs):
        form = EnrollmentForm()
        now = timezone.now().date()
        print(form)
        grade = requests.get(WEBService+'grade/')
        grade=grade.json()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            student=kwargs['student']
            student = requests.get(WEBService + 'student' + '/' + student)
            student = student.json()
            student=str(student['id'])
            grade = requests.get(WEBService + 'grade' + '/' + obj.grade.id)
            grade = grade.json()
            grade = str(grade['id'])
            set_data = '{"rode":"' + str(obj.rode) + '",' \
                    ' "tariff": "'+str(obj.tariff)+'",' \
                    ' "total": "'+str(obj.total)+'",' \
                    ' "monthly": "'+str(obj.monthly)+'",' \
                    ' "remaining": "'+str(obj.remaining)+'",' \
                    ' "grade": "'+grade+'",' \
                    ' "period": "'+str(obj.period)+'",' \
                    ' "student": "'+student+'",' \
                    ' "payment": '+str(obj.payment)+'}'

            set_data=json.loads(str(set_data))
            ll=requests.post(WEBService+'enrollment/', data=set_data)
            ll= ll.json()
            #form.save()
            return redirect('module_reports:enrollment-report', id=ll['id'])
        else:
            print(form.is_valid())
            print(form.errors)
            form = EnrollmentForm(request.POST)
            #return redirect('module_admin:admission_enrollment_set', rut=kwargs['rut'], student=kwargs['student'])

            return render(request, self.template, locals())