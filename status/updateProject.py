from models import Project
from django.conf import settings

from datetime import timedelta

def updateProjects():
    #Get settings
    short_p = settings.MISSED_PINGS_SHORT
    long_p = settings.MISSED_PINGS_LONG

    projects = Project.objects.all()
    for proj in projects:
        status = 0
        if proj.active:
            delta = timedelta(seconds=proj.alertAfter_s)
            now = datetime.now()
            lp = proj.lastPing
            if lp:
                if lp + (delta * long_p) < now:
                    #missed long ping
                    status = 3
                elif lp + (delta * short_p) < now:
                    #missed short ping
                    #TODO: Send email if not yet sent
                    status = 2
                else:
                    #We're good
                    status = 1
        proj.status = status
        proj.save()
