from django.db         import models



class AuditFields(models.Model):
    
    title               = models.CharField('TITLE',             max_length=250)
    photo               = models.ImageField('PHOTO',            upload_to='images/')
    bool_deleted        = models.BooleanField('IS DELETED?',    default=False)
    
    class Meta:
        abstract = True
