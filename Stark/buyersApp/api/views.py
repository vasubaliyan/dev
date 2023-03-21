from rest_framework import viewsets
from .serializers import *
from buyersApp.models import Buyers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action

import pyotp
import base64




class LoginOtpViewset(viewsets.ModelViewSet):
    queryset=Buyers.objects.all()
    serializer_class=LoginOtpSerializer


    @action(detail=False, methods=['post'])
    def login(request):
        pass
    
        


