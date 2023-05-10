from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
'''ModelViewSet class crate CRUD behind the scene without defining 
create(), get(), update() and delete() methods,'''
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    '''Add BasicAuthentication to this API, so that only authenticated user
    can access this API. user try to access API with user name & password.
    In BasicAuthentication credential is user name and password'''
    authentication_classes = [BasicAuthentication] 
    # Give all kinds of autheticated user permission to access API
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# Globally defined authentication is applicable for evry view class
'''
class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication] 
    # Give all kinds of users permission to access API
    permission_classes = [AllowAny]'''

# Globally defined authentication is applicable for evry view class
'''
class StudentModelViewSet3(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer'''
