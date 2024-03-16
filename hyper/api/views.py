from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDoctor, IsGeneralManager, IsAssistant
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
