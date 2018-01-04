# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import json
from CMDBpro.models import dcos_host
from CMDBpro.models import components
from Ansible import hostoption

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
        hostip=item.host_ip
        findcomp=components.objects.filter(hostname=hostip).values('component').distinct()
        comptext=''
        for comp in findcomp:
            comptext+= comp['component']+';'
        if comptext!='':
            print comptext
        hostlist.append({"hostip":item.host_ip,"hostname":item.host_name,"env":item.env,"comp":comptext})
    host_res = {"hostlist": hostlist}
    return HttpResponse(json.dumps(host_res), content_type='application/json')

def testping(request):
    testiplist=request.GET.get("iplist").split(';')
    pingresult=[]
    for item in testiplist:
        state=0
        info=''
        pres=hostoption.ping(item)
        if len(pres['contacted'].items())==0 and len(pres['dark'].items())==0:
            state=1
            info='ip not in ansible inventory'
        elif len(pres['dark'].items())==0 and pres['contacted'].items()[0][0]==item:
            state=0
            info='ping ok'
        elif pres['dark'].items()[0][0]!='':
            state=1
            info='host is unknown, check the ansible inventory!'
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
        info='host is unknown, check the ansible inventory!'
    ret['state']=state
    ret['info']=info
    return ret

def md5check(request):
    testiplist=request.GET.get("iplist").split(';')
    filename=request.GET.get("filename")
    md5result=[]
    for item in testiplist:
        result=getinfo(hostoption.md5sum(item,filename),item)
        md5result.append({"hostip":item,"state":result['state'],"info":result['info']})
    md5_res = {"md5res":md5result}
    return HttpResponse(json.dumps(md5_res), content_type='application/json')

def showlogs(request):
    testiplist=request.GET.get("iplist").split(';')
    logresult=[]
    for item in testiplist:
        result=getinfo(hostoption.findlogs(item),item)
        logresult.append({"hostip":item,"state":result['state'],"info":result['info']})
    log_res = {"logres":logresult}
    return HttpResponse(json.dumps(log_res), content_type='application/json')

def testfile(request):
    filename=request.GET.get("filename")
    hostip=request.GET.get("hostip")
    result=getinfo(hostoption.filetest(hostip,filename),hostip)
    testres={"hostip":hostip,"state":result['state'],"info":result['info']}
    test_res={"testres":testres,'state':result['state']}
    return HttpResponse(json.dumps(test_res), content_type='application/json')

def testdest(request):
    destpath=request.GET.get("destpath")
    iplist=request.GET.get("iplist").split(';')
    destres=[]
    flag=0
    for destip in iplist:
        result=getinfo(hostoption.desttest(destip,destpath),destip)
        if result['state']!=0:
            flag=1
        destres.append({"hostip":destip,"state":result['state'],"info":result['info']})
    dest_res = {"destres":destres,'state':flag}
    return HttpResponse(json.dumps(dest_res), content_type='application/json')

def copyfile(request):
    hostip=request.GET.get("hostip")
    filename=request.GET.get("filename")
    iplist=request.GET.get("iplist").split(';')
    destpath=request.GET.get("destpath")
    flag=0
    testres=[]
    for destip in iplist:
        result=getinfo(hostoption.desttest(destip,destpath),destip)
        if result['state']!=0:
            flag=1
            testres.append({"hostip":destip,"state":result['state'],"info":result['info']})
    testresult=getinfo(hostoption.filetest(hostip,filename),hostip)
    if testresult['state']!=0:
        flag=1
        testres.append({"hostip":hostip,"state":testresult['state'],"info":testresult['info']})
    if flag==1:
        copy_res={"copyres":testres,'state':1}
        return HttpResponse(json.dumps(copy_res), content_type='application/json')
    else:
        copyres=[]
        for destip in iplist:
            result=getinfo(hostoption.filecopy(destip,hostip,filename,destpath),destip)
            copyres.append({"hostip":destip,"state":result['state'],"info":result['info']})
        copy_res = {"copyres":copyres,'state':0}
        return HttpResponse(json.dumps(copy_res), content_type='application/json')
