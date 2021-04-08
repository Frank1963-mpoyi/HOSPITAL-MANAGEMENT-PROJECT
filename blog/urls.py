
from django.urls            import      path
from .view_appointment      import      view_appointment, update_appointment, delete_appointment, add_appointment 
from .view_doc              import      view_doctor , add_doctor, delete_doctor, update_doctor
from .view_patient          import      view_patient, delete_patient, add_patient, update_patient
from .views   import (
    home_view, 
    contact_view,
    about_us , 
    admin_login, 
    login_admin,
    logout_admin,

    )



urlpatterns = [
    
    path('',            home_view,      name='home'),
    path('about/',      about_us,       name='about_us'),
    path('contact/',    contact_view,   name='contact_view'),
    
    #=== Auth ====
    path('login/',       login_admin,   name='login'),
    path('logout/',      logout_admin,  name='logout'),
    path('admin-login/', admin_login,   name='admin_login'),

    
    
    #==== Doctor ====
    path('view_doctor/', view_doctor,   name='view_doctor'),
    path('add_doctor/',  add_doctor,    name='add_doctor'),
    path('update_doctor/<int:pk>', update_doctor,  name='update_doctor'),
    path('delete_doctor/<int:pk>', delete_doctor,   name='delete_doctor'),
    
    
    #==== Patient =====
    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/',  add_patient,  name='add_patient'),
    path('update_patient/<int:pk>',update_patient, name='update_patient'),
    path('delete_patient/<int:pk>',delete_patient,  name='delete_patient'),
    
    
    #==== Appointment ==
    path('view_appointment/', view_appointment,     name='view_appointment'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('update_appointment/<int:pk>', update_appointment,   name='update_appointment'),
    path('delete_appointment/<int:pk>',delete_appointment,      name='delete_appointment'),
    


]
