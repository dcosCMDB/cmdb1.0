# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import json
from CMDBpro.models import Loginuser,components
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def changecomp(request):
    if request.POST:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = Loginuser.objects.filter(username__exact = username,password__exact = password)
        if user:
            context = data['context']
            for k in context:
                for item in context[k]:
                    for i in item:
                        line={}
                        line['hostname']=item['hostname']
                        line['component']=k
                        line['tag']=i
                        line['value']=item[i]
                        print line
                        comp=components(hostname=line['hostname'],component=line['component'],tag=line['tag'],value=line['value'])
                        comp.save()
            test_res = {"test_res": context}
            return HttpResponse(json.dumps(test_res), content_type='application/json')
        else:
            test_res = {"test_res": 'login failed'}
            return HttpResponse(json.dumps(test_res), content_type='application/json')
    else:
        test_res = {"test_res": 'not post'}
        return HttpResponse(json.dumps(test_res), content_type='application/json')
