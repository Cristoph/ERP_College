from django.contrib import admin
from .models import UserProfile, Subject, Grade, Teacher, Student, Qualification, Attorney


admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
#admin.site.register(Administrative)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attorney)
admin.site.register(Qualification)

