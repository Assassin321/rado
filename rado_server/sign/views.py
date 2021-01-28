from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import json
from common.models import *
# Create your views here.
def signUp(params):
    username = params["email"]
    password = params["password"]
    User.objects.create_superuser(username=username,password=password)
    return JsonResponse({"seccuss sign up":1})


def signIn(requset):
    params = json.loads(requset.body)
    userName = params["email"]
    passWord = params["password"]
    user = authenticate(username=userName, password=passWord)
    if user is not None:

        if user.is_active:
            if user.is_superuser:
                login(requset,user)
                requset.session["usertype"] ="svip"
                return JsonResponse({"seccuss sign up":1})
            else:
                return JsonResponse({"not svip":0})
        else:
            return JsonResponse({'not actice':0})
    else:
        return JsonResponse({'not right num':0})

def dispatcher(requset):
    params = json.loads(requset.body)
    action = params["action"]
    if action=="signup":
        return (signUp( params))
    elif action == "signin":
        return (signIn(requset))
    return JsonResponse({"ret":1})