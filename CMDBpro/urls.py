"""CMDBpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view as login_views
from hostlist import views as host_views
from bashlist import views as bash_views
from cronlist import views as cron_views
from componentlist import views as component_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login', login_views.login),
    url(r'^logout', login_views.logout),
    url(r'^index', login_views.index),

    url(r'^showhost', host_views.showhost),
    url(r'^searchhost', host_views.searchhost),
    url(r'^testping', host_views.testping),
    url(r'^md5check', host_views.md5check),

    url(r'^showbash', bash_views.showbash),

    url(r'^showcron', cron_views.showcron),

    url(r'^changecomp', component_views.changecomp),

]
