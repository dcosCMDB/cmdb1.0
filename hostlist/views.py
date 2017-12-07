# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import json
from CMDBpro.models import dcos_host
from Ansible.hostoption import ping

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
            info='not known'
        pingresult.append({"hostip":item,"state":state,"info":info})
    ping_res = {"pingres":pingresult}
    return HttpResponse(json.dumps(ping_res), content_type='application/json')
