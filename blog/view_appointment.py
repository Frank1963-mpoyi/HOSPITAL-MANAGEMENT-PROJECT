from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Appointment, Patient, Doctor
from .forms import DoctorModelForm, AppointmentModelForm,  PatientModelForm




def view_appointment(request):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    Ap = Appointment.objects.all() # object App must not have the same name as class name 
    template_name =  'blog/view_appointment.html'
    context = {'Ap': Ap}
    return render(request, template_name , context)



def update_appointment(request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    
    appointment = Appointment.objects.get(id=pk)
    form =  AppointmentModelForm(request.POST or None , instance=appointment)
    if form.is_valid():
        form.save()
        return redirect(view_appointment)
    context = {'form': form}
    return render(request, 'blog/update_appointment.html', context)




def delete_appointment(request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    app = get_object_or_404(Appointment, id = pk)
    app.delete()
    return redirect(view_appointment)




def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == "POST":
        d = request.POST.get('doctor')
        p = request.POST.get('patient')
        dat = request.POST.get('date')
        tim = request.POST.get('time')
        doctor_b = Doctor.objects.filter(name=d).first()
        patient_b = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(Doctor = doctor_b, Patient = patient_b, date=dat, time=tim)
            error = 'no'
        except:
            error = 'yes'
            
    context = {
        'error': error,
        'doctor': doctor1,
        'patient': patient1
    }        
    return render (request, 'blog/add_appointment.html', context)
