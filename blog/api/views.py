from    blog.models                     import Doctor, Patient, Appointment

from    .serializers                    import (
    UserSerializer,
    DoctorSerializer,
    PatientSerializer,
    AppointmentSerializer,
    )

from    rest_framework                  import  viewsets
from    rest_framework.authentication   import  TokenAuthentication                 
from    rest_framework.permissions      import  IsAuthenticated
#import built in django user model
from    django.contrib.auth.models      import  User







class DoctorViewSet(viewsets.ModelViewSet):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    

class PatientViewSet(viewsets.ModelViewSet):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)



class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer