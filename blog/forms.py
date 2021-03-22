from django import forms
from .models import Patient, Doctor, Appointment






class PatientModelForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields =  '__all__'



class DoctorModelForm(forms.ModelForm):
    # mobile = forms.IntegerField(required = False) 
    #special = forms.CharField(required = False) 

    def __init__(self, *args, **kwargs):
        super(DoctorModelForm, self).__init__(*args, **kwargs)
        #self.fields['special'].required = False
        self.fields['mobile'].required = False
        self.fields['name'].required = False
    
    class Meta:
        model = Doctor
        fields = ['name', 'mobile', 'special']
    
    


class AppointmentModelForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields =  '__all__'