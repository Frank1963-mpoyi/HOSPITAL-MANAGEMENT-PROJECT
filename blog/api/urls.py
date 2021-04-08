
from django.urls import path, include 
from .views import PatientViewSet, DoctorViewSet, UserViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('patient', PatientViewSet, basename='patient')
router.register('doctor', DoctorViewSet, basename='doctor')
# it for userviewset
router.register('users', UserViewSet)


urlpatterns = [
    
    path('', include(router.urls)), # include default router here

]





























