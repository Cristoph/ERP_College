from django.shortcuts import render
from ModuleCommon.models import Qualification
from django.views import View

class ReportQualifications(View):
    template = 'ModuleReports/report-qualifications.html'

    def get(self, request, *args, **kwargs):
        qualifications = Qualification.objects.filter(student=kwargs['pk']).order_by('subject')
        subject = []
        for lo in qualifications:
            val=False
            for sub in subject:
                if lo.subject == sub:
                    val=True
            if val==False:
                subject += [lo.subject]
        values={}
        for sub in subject:
            num = 0
            qualification=qualifications.filter(subject=sub).order_by('position')
            last = int(qualification.last().position)
            values[sub]={}
            print(qualification[num])
            while (num < last):
                #print(qualification[num])
                #if int(qualification[1])>0:
                 #   print('jhj')
                #values[sub][num]=
                num+=1
        data = {'qualifications': qualifications,
               'subject': subject}
        return render(request, self.template, locals(), data)