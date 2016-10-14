from models import Project
from django.conf import settings
import pytz
from ipware.ip import get_real_ip
from datetime import datetime, timedelta

def updateProjects():
    #Get settings
    short_p = settings.MISSED_PINGS_SHORT
    long_p = settings.MISSED_PINGS_LONG

    projects = Project.objects.all()
    for proj in projects:
        status = 0
        if proj.active:
            delta = timedelta(seconds=proj.alertAfter_s)
            now = datetime.now(pytz.utc)
            lp = proj.lastPing
            if lp:
                if lp + (delta * long_p) < now:
                    #missed long ping
                    status = 3
                elif lp + (delta * short_p) < now:
                    #missed short ping
                    #TODO: Email for offline
                    project.notified = True
                    status = 2
                else:
                    #Online
                    status = 1
        proj.status = status
        proj.save()

def pingProject(project, request):
    ip = get_real_ip(request)
    now = datetime.now(pytz.utc)
    project.lastPing = now
    project.lastPingIP = ip
    if project.status > 1:
        #If project was offline, set it back to online
        project.notified = False
        project.status = 1
        #TODO: Email for back online
    project.save()
    return true