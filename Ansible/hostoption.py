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

def md5sum(hostip):
	md5runner = ansible.runner.Runner(
		module_name='shell',
		module_args='',
		pattern=hostip,
		forks=10)
	pingres = md5runner.run()
	return md5res