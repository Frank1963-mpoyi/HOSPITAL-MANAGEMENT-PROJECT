from django.contrib import admin
from .models import (
    Doctor, 
    Patient, 
    Appointment, 
    MeetOurTeem, 
    OtherService,
    MedicalService
    )



admin.site.register(
    [
        Doctor,
        Patient, 
        Appointment,
        OtherService,
        MeetOurTeem,
        MedicalService
        
        ]
    )
