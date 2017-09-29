from django import forms
from  ModuleCommon.models import Attorney, Enrollment


# class AttorneyForm(forms.Form):
#    url = forms.URLField()

class RutForm(forms.ModelForm):

	class Meta:
		model=Attorney
		fields=[
            'rut',
        ]

		labels={
			'rut':'Rut',
        }
		widgets={
            'rut' : forms.TextInput(attrs={'class':'form-control'}),
        }


class AttorneyForm(forms.ModelForm):

	class Meta:
		model=Attorney
		fields=[
            'rut',
            'first_name',
            'last_name',
            'gender',
            'address',
            'email',
            'birthdate',
            'age',
            'phone',
            'cellphone',
		]
		labels={
			'rut':'Rut',
			'first_name':'First_name',
			'last_name':'Last_name',
			'gender':'Gender',
			'address':'Address',
			'email':'Email',
			'birthdate':'Birthdate',
            'age': 'Age',
            'phone': 'Phone',
            'cellphone': 'Cellphone',
		}
		widgets={
            'rut' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'birthdate' : forms.SelectDateWidget(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'cellphone' : forms.TextInput(attrs={'class':'form-control'}),
                }


class EnrollmentForm(forms.ModelForm):

	class Meta:
		model=Enrollment
		fields=[
            'rode',
            'tariff',
            'monthly',
            'total',
            'remaining',
            'grade',
            'period',
            'student',
            'payment'
		]
		labels={
			'rode':'Rode',
			'tariff':'Tariff',
			'monthly':'Monthly',
			'total':'Total',
			'remaining':'Remaining',
            'grade': 'Grade',
            'period': 'Period',
            'student': 'Student',
            'payment': 'Payment'
		}
		widgets={
            'rode' : forms.TextInput(attrs={'class':'form-control'}),
            'tariff' : forms.TextInput(attrs={'class':'form-control'}),
            'monthly' : forms.TextInput(attrs={'class':'form-control'}),
            'total' : forms.TextInput(attrs={'class':'form-control'}),
            'remaining' : forms.TextInput(attrs={'class':'form-control'}),
            'grade' : forms.Select(attrs={'class':'form-control'}),
            'period' : forms.Select(attrs={'class':'form-control'}),
            'student' : forms.TextInput(attrs={'class':'form-control'}),
            'payment' : forms.TextInput(attrs={'class':'form-control'}),
                }

