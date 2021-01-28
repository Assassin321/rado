from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from common.models import *


# Create your views here.
def allData(request):
    if request.method == 'POST':
        try:
            # fname=request.POST.get("name","default.jpg")
            rid = request.POST.get("id", "0")
            photo = request.FILES.get("file")
            RadoData.objects.create(radoData=photo, rid_id=rid)
            return JsonResponse({"ret": 1, 'msg': 'Success'})
        except:
            return JsonResponse({"ret": 0, 'msg': 'Something went wrong during uploading'})
