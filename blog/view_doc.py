from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Doctor
from .forms import DoctorModelForm







def view_doctor(request):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    context = {'doc':doc}
    template_name =  'blog/view_doctor.html'
    return render(request, template_name , context)


def update_doctor (request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        patient = DoctorModelForm.objects.get(id=pk)
        form =  DoctorModelForm(request.POST or None , instance=patient)
        if form.is_valid():
            form.save()
            #return redirect(view_patient)
    return redirect( view_doctor)


def delete_doctor(request, pk=None):
    # if you are not staff member they must redirect you in login
    if not request.user.is_staff:
        return redirect('login')
    doc = get_object_or_404(Doctor, id = pk)
    doc.delete()
    return redirect( view_doctor)




def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        s = request.POST.get('special')

        try:
            Doctor.objects.create(name=n, mobile=m, special=s)
            error = 'no'
        except:
            error = 'yes'
            
    context = {
        'error': error
    }        
    return render (request, 'blog/add_doctor.html', context)
