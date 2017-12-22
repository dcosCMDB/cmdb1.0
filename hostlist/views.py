# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import json
from CMDBpro.models import dcos_host
from Ansible.hostoption import ping,md5sum,findlogs

def showhost(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        response = HttpResponseRedirect('/showhost')
        return render(request, 'hosttable.html')
    else:
        response = HttpResponseRedirect('/')
        return render(request, 'login.html')

def searchhost(request):
    findall=dcos_host.objects.all()
    hostlist=[]
    for item in findall:
    	hostlist.append({"hostip":item.host_ip,"hostname":item.host_name,"env":item.env,"cpu":item.cpu,"mem":item.mem,"filesys":item.filesys})
    host_res = {"hostlist": hostlist}
    return HttpResponse(json.dumps(host_res), content_type='application/json')

def testping(request):
    testiplist=request.GET.get("iplist").split(';')
    pingresult=[]
    for item in testiplist:
        state=0
        info=''
        pres=ping(item)
        if len(pres['contacted'].items())==0 and len(pres['dark'].items())==0:
            state=1
            info='ip not in ansible inventory'
        elif len(pres['dark'].items())==0 and pres['contacted'].items()[0][0]==item:
            state=0
            info='ping ok'
        elif pres['dark'].items()[0][0]!='':
            state=1
            info='unknown'
        pingresult.append({"hostip":item,"state":state,"info":info})
    ping_res = {"pingres":pingresult}
    return HttpResponse(json.dumps(ping_res), content_type='application/json')

def getinfo(result,hostip):
    ret={}
    state=0
    info=''
    if len(result['contacted'].items())==0 and len(result['dark'].items())==0:
        state=1
        info='ip not in ansible inventory'
    elif len(result['dark'].items())==0 and result['contacted'].items()[0][0]==hostip:
        stdout=result['contacted'].items()[0][1]['stdout']
        stderr=result['contacted'].items()[0][1]['stderr']
        if stderr=='':
            info=stdout
        else:
            state=1
            info=stderr
    elif result['dark'].items()[0][0]!='':
        state=1
        info='unknown'
    ret['state']=state
    ret['info']=info
    return ret

def md5check(request):
    testiplist=request.GET.get("iplist").split(';')
    md5result=[]
    for item in testiplist:
        result=getinfo(md5sum(item,'/tmp/test.py'),item)
        md5result.append({"hostip":item,"state":result['state'],"info":result['info']})
    md5_res = {"md5res":md5result}
    return HttpResponse(json.dumps(md5_res), content_type='application/json')

def showlogs(request):
    testiplist=request.GET.get("iplist").split(';')
    logresult=[]
    for item in testiplist:
        result=getinfo(findlogs(item),item)
        logresult.append({"hostip":item,"state":result['state'],"info":result['info']})
    log_res = {"logres":logresult}
    return HttpResponse(json.dumps(log_res), content_type='application/json')