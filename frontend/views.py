from models import *
import datetime
# Create your views here.

def new_script(name,body):
    script=Script(name=name,body=body)
    script.save()
    id=script.id
    return {"status":"success","id":id}

def save_script(id,body):
    script=Script.get_by_id(id)
    script.body=body
    script.save()
    return {"status":"success"}

def save_log(id,starttime,endtime,output):
    duration=endtime-starttime
    starttime=datetime.datetime.fromtimestamp(starttime)
    endtime=datetime.datetime.fromtimestamp(endtime)
    log=ExecutionLog(script_id=id, starttime=starttime, endtime=endtime, duration=duration, output=output)
    log.save()
    return {"status":"success"}

def get_scriptnames():
    script=Script.select().order_by('id')
    data=[]
    for i in script:
        data.append([i.id,i.name])
    return {"data":data}

def get_scriptbody(id):
    script=Script.get_by_id(id)
    body=script.body
    return {"body":body}

def delete_script(id):
    script=Script.get_by_id(id)
    script.delete_instance()
    return {"status":"success"}