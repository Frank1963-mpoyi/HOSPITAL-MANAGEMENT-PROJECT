
from django.urls import path
from .view_doc import view_doctor , add_doctor, delete_doctor#, update_doctor
from .view_patient import view_patient, delete_patient, add_patient#, update_patient
from .views import (
    home_view, 
    contact_view,
    about_us , 
    admin_login, 
    login_admin,
    logout_admin,

    )





urlpatterns = [
    
    path('contact/', contact_view, name='contact_view'),
    path('admin-login/', admin_login, name='admin_login'),
    path('login/', login_admin, name='login'),
    path('logout/', logout_admin, name='logout'),
    path('about/', about_us, name='about_us'),
    path('', home_view, name='home'),
    
    path('view_doctor/', view_doctor, name='view_doctor'),
    #path('update_doctor/<int:pk>', update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>', delete_doctor, name='delete_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    
    path('view_patient/', view_patient, name='view_patient'),
    #path('update_patient/<int:pk>',update_patient, name='update_patient'),
    path('delete_patient/<int:pk>',delete_patient, name='delete_patient'),
    path('add_patient/', add_patient, name='add_patient'),
]
