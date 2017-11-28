# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Loginuser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class dcos_host(models.Model):
    id = models.CharField('主机ID', max_length=255, primary_key=True)
    host_ip = models.CharField('主机', max_length=255)
    host_name = models.CharField('主机名', max_length=255)
    env = models.CharField('区域', max_length=255)
    cpu = models.CharField('主机CPU', max_length=255)
    mem = models.CharField('主机内存', max_length=255)
    filesys = models.CharField('文件系统', max_length=255)
