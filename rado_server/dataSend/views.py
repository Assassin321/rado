import os

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
import json
from common.models import *


def getRados(request):
    rados = RadoData.objects.order_by("rid_id").values("rid_id").distinct()
    data = {}
    data["radoNum"] = len(rados)
    radoData = []
    for each in rados:
        eachdata = {}
        eachdata["id"] = each["rid_id"]
        rado = RadoData.objects.filter(rid_id=each["rid_id"]).order_by("-UpdateTime").first()
        photo = str(rado.radoData)
        time = rado.UpdateTime
        eachdata["radoData"] = photo
        eachdata["time"] = time
        radoData.append(eachdata)
    data["rado"] = radoData
    return JsonResponse({"AllRado": data})


def getRadoInfo(request):
    rid = request.GET.get("rid", "")
    radoData = {}
    rado = RadoData.objects.filter(rid_id=rid).order_by("-UpdateTime").first()
    photo = str(rado.radoData)
    time = rado.UpdateTime
    radoData["id"] = rid
    radoData['radoData'] = "media/" + photo
    radoData['time'] = time
    js = JsonResponse({"Rado": radoData})
    js.set_cookie("sessions", "123456554",expires="6000")
    return js


def Download(request):
    photo = request.GET.get("photo", "")
    filename = photo[photo.rindex('/') + 1:]
    path = os.path.join(os.getcwd(), 'media', photo.replace('/', '\\'))
    with open(path, 'rb') as f:
        response = HttpResponse(f.read())
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename=' + photo.replace('/', '\\')[18:]
    return response


def getBoats(request):
    bid = request.GET.get("bid", "")
    rid = RadoBoat.objects.filter(bid=bid)[0].rid
    boats = BoatRecord.objects.filter(rid_id=bid).order_by("-BoatTime").first()
    Data = []
    for boat in boats:
        boatData = {}
        boatData["Bid"] = boat.bid
        boatData['BoatPosition'] = [boat.x, boat.y]
        boatData['time'] = str(boat.BoatTime)
        Data.append(boatData)

    return JsonResponse({"Boat": Data})


def test(request):
    session = request.COOKIES["session"]
    return HttpResponse(session)

