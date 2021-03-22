from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment


def home_view(request):
    template_name =  'blog/home.html'
    return render(request, template_name )



def contact_view(request):
    template_name =  'blog/contact.html'
    return render(request, template_name )



def about_us(request):
    template_name =  'blog/about.html'
    return render(request, template_name )


def admin_login (request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    a=0
    
    for i in doctor:
        d = d + 1
        
    for i in  patient:
        p+=1
        
    for i in appointment:
        a+=1
    
    context = {
        'd': d,
        'p': p,
        'a': a
    }
    return render (request, 'blog/admin_login.html', context)



def login_admin(request):
    error = ""
    if request.method == "POST":
        username_1 = request.POST.get('uname')
        password_1 = request.POST.get('pwd')
        # u = request.Post['uname'] the request.Post object is a dictionary that why we grab the key name in frontend in order to get data
        user = authenticate(username=username_1, password=password_1)
        try:
            if user.is_staff:
                login(request, user)
                error ="no"
            else:
                error ="yes"
        except:
            error = "yes"
    context = {
        'error': error
    }        
    return render (request, 'blog/login.html', context)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')









# request.Post is a Dictionary 
# that why we grab the data with the key name from frontend to get the value
mpoyi = {
    "papa": "Mpoyi",
    "maman": "Mitongu"
}

print(mpoyi.get("papa"), mpoyi["maman"])