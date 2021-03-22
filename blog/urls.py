
from django.urls import path
from .views import (
    home_view, 
    contact_view,
    about_us , 
    admin_login, 
    login_admin,
    logout_admin,
    view_doctor,
    add_doctor,
    delete_doctor,
    )





urlpatterns = [
    
    path('contact/', contact_view, name='contact_view'),
    path('admin-login/', admin_login, name='admin_login'),
    path('login/', login_admin, name='login'),
    path('logout/', logout_admin, name='logout'),
    path('about/', about_us, name='about_us'),
    path('', home_view, name='home'),
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('delete_doctor/<int:pk>', delete_doctor, name='delete_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
]
