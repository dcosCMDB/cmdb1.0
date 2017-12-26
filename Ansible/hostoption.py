# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ansible.runner

def ping(hostip):
	pingrunner = ansible.runner.Runner(
		module_name='ping',
		module_args='',
		pattern=hostip,
		forks=10)
	pingres = pingrunner.run()
	return pingres

def md5sum(hostip,filename):
    md5runner = ansible.runner.Runner(
        module_name='shell',
        module_args='md5sum '+filename,
        pattern=hostip,
        forks=10)
    md5res = md5runner.run()
    return md5res

def findlogs(hostip):
    logrunner = ansible.runner.Runner(
        module_name='shell',
        module_args='find /data/logs -name "*.log*"|xargs du -h|sort -hr|head -10',
        pattern=hostip,
        forks=10)
    logres = logrunner.run()
    return logres

def filetest(hostip,filename):
    testrunner = ansible.runner.Runner(
        module_name='shell',
        module_args='ls '+filename,
        pattern=hostip,
        forks=10)
    testres = testrunner.run()
    return testres

def desttest(hostip,destpath):
    testrunner = ansible.runner.Runner(
        module_name='shell',
        module_args='ls '+destpath,
        pattern=hostip,
        forks=10)
    testres = testrunner.run()
    return testres

def filecopy(destip,hostip,filename):
    testrunner = ansible.runner.Runner(
        module_name='shell',
        module_args='scp '+hostip+':'+filename+' '+destip,
        pattern=hostip,
        forks=10)
    testres = testrunner.run()
    return testres