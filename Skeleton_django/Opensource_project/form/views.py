# from django.shortcuts import render
import json
import argparse
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets # vieset import
import base64
from .serializers import UserSerializer # 생성한 serializer import
from .models import User # User model import
import os
@ensure_csrf_cookie

def result(request):
    if request.method == "POST":
        if request.POST['options'] and request.POST['file']:
            options = json.loads(request.POST['options'])
            print(type(options),options)

            url = request.POST['file'].split(",")[1]
            encoded = str(url).encode('utf-8')
            with open('out.png','wb') as file:
                de = base64.decodebytes(encoded)
                file.write(de)
            start_path = 'python "CV_skeleton_provider/SkeletonProvider.py"'
            file_path = '  --source "out.png"'
            os.system('pwd')
            os.system(start_path+file_path)

    name = 'd'
    return JsonResponse(name,safe=False)

class UserViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #print(queryset)
