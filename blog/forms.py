from django import forms
from .models import Patient






class PatientModelForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields =  '__all__'



class DoctorModelForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields =  '__all__'