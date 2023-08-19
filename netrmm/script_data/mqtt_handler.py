from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
import datetime
# Create your views here.

def test(request):
    print("testing is fine")
    # return HttpResponse("testing ok")

def new_script(request):
    name=request["name"]
    body=request["body"]
    script=Script(name=name,body=body)
    script.save()
    id=script.id
    # return JsonResponse({"status":"success","id":id})

def save_script(request):
    id=int(request["id"])
    body=request["body"]
    script=Script.objects.get(id=id)
    script.body=body
    script.save()
    # return JsonResponse({"status":"success"})

def save_log(request):
    id=int(request["id"])
    starttime=float(request["starttime"])
    endtime=float(request["endtime"])
    output=request["output"]
    duration=endtime-starttime
    starttime=datetime.datetime.fromtimestamp(starttime)
    endtime=datetime.datetime.fromtimestamp(endtime)
    log=ExecutionLog(script_id=id, starttime=starttime, endtime=endtime, duration=duration, output=output)
    log.save()
    # return JsonResponse({"status":"success"})

def delete_script(id):
    script=Script.objects.get(id=id)
    script.delete()
    # return JsonResponse({"status":"success"})