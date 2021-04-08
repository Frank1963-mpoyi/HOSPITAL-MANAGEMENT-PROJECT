from    django.db               import      models
from    core.model_mixins       import      AuditFields







class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.doctor.name
    
    
class MedicalService(AuditFields):
    
    
    def __str__(self):
        return self.title
    

class OtherService(models.Model):
    name               = models.CharField('NAME',         max_length=250, default="name")
    images               = models.ImageField('IMAGE',     upload_to='images/', default="mpoyi.jpg")
    
    def __str__(self):
        return self.name
    

class MeetOurTeem(AuditFields):
    
    
    def __str__(self):
        return self.title
    