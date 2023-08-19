from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
import datetime
# Create your views here.

def test(request):

    print("testing is fine")
    return HttpResponse("testing ok")

def new_script(request):

    name=request.POST["name"]
    body=request.POST["body"]
    script=Script(name=name,body=body)
    script.save()
    id=script.id
    return JsonResponse({"status":"success","id":id})

def save_script(request):

    id=int(request.POST["id"])
    body=request.POST["body"]
    script=Script.objects.get(id=id)
    script.body=body
    script.save()
    return JsonResponse({"status":"success"})

def save_log(request):

    id=int(request.POST["id"])
    starttime=float(request.POST["starttime"])
    endtime=float(request.POST["endtime"])
    output=request.POST["output"]
    duration=endtime-starttime
    starttime=datetime.datetime.fromtimestamp(starttime)
    endtime=datetime.datetime.fromtimestamp(endtime)
    log=ExecutionLog(script_id=id, starttime=starttime, endtime=endtime, duration=duration, output=output)
    log.save()
    return JsonResponse({"status":"success"})

def get_scriptnames(request):

    script=Script.objects.all().order_by('id')
    data=[]
    for i in script:
        data.append([i.id,i.name,i.body])
    return JsonResponse({"data":data})

def get_scriptbody(request,id):

    script=Script.objects.get(id=id)
    body=script.body
    return JsonResponse({"body":body})

def delete_script(request,id):

    script=Script.objects.get(id=id)
    script.delete()
    return JsonResponse({"status":"success"})