from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Patient
from .forms import  PatientModelForm





def view_patient(request):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.all()
    context = {'patient': patient}
    template_name =  'blog/view_patient.html'
    return render(request, template_name , context)



def update_patient(request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        patient = Patient.objects.get(id=pk)
        form =  PatientModelForm(request.POST or None , instance=patient)
        if form.is_valid():
            form.save()
            return redirect(view_patient)
    context = {'form': form}
    return render(request, 'blog/update.html', context)




def delete_patient(request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    doc = get_object_or_404(Patient, id = pk)
    doc.delete()
    return redirect( view_patient)




def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST.get('name')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')

        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = 'no'
        except:
            error = 'yes'
            
    context = {
        'error': error
    }        
    return render (request, 'blog/add_patient.html', context)
