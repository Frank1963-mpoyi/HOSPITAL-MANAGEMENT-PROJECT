from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
    return render (request, 'blog/admin_login.html')

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