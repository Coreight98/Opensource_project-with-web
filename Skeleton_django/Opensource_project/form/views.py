# from django.shortcuts import render
import json
import argparse
import time

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
    name = ''
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
            file_path = '  --source "out.png" --gray {} --gamma {} --back {} --autolocation {} --b_propo {}' .format(options['gray'],float(options['gamma']),options['back'],options['autolocation'],options['b_propo'])
            os.system('pwd')
            os.system(start_path+file_path)
            time.sleep(3)
            with open("result.jpg", "rb") as img_file:
                my_string = base64.b64encode(img_file.read()).decode('utf8')
            print(my_string)
            name = my_string
    return JsonResponse({
        'name' : 'data:image/jpeg;base64,'+name,
    }, json_dumps_params = {'ensure_ascii': True})

class UserViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #print(queryset)
