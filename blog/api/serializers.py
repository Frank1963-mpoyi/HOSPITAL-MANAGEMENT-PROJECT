from    rest_framework                  import  serializers
from    django.contrib.auth.models      import  User
from    blog.models                     import  (
    Appointment,
    Doctor,
    Patient,
    )
#if there is new user registration he must get a token
from rest_framework.authtoken.views import Token






class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) 
        return user
    








