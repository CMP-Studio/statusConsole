from models import Project, Downtime, Contact
from django.conf import settings
import pytz
from ipware.ip import get_real_ip
from datetime import datetime, timedelta
from django.core.mail import send_mail

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
                    if not proj.notified:
                        sendAlertStart(proj)
                        proj.notified = True
                    #Create a downtime
                    startDowntime(proj)

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
        if project.notified:
            sendAlertEnd(project)
            project.notified = False
        project.status = 1
        endDowntime(project)
    project.save()
    return True

def startDowntime(project):
    #First stop any other ongoing downtimes
    activeDts = Downtime.objects.filter(project=project, ongoing=True)
    for dt in activeDts:
        dt.ongoing = False
        dt.save()
    #Now create a new downtime
    newDt = Downtime(project=project)
    newDt.save()

def endDowntime(project):
    activeDts = Downtime.objects.filter(project=project, ongoing=True)
    for dt in activeDts:
        dt.down_end = datetime.now()
        dt.ongoing = False
        dt.save()

def getAlertContacts(project):
    emails = []
    #Add owners email
    emails.append(project.owner.email)
    contacts = project.alertedContacts.all()
    for c in contacts:
        emails.append(c.email)
    return emails


def sendAlertStart(project):
    #First gather addresses
    to = getAlertContacts(project)
    name = project.name

    now = datetime.utcnow()
    eastern = pytz.timezone('US/Eastern')
    local = now.replace(tzinfo=pytz.utc).astimezone(eastern)
    strlocal = local.strftime(settings.DATETIME_FORMAT)

    lp = project.lastPing
    lplocal = lp.replace(tzinfo=pytz.utc).astimezone(eastern)
    strlp = local.strftime(settings.DATETIME_FORMAT)

    send_mail("Application Down: " + name,"Notice: " + name + " stopped pinning on " + strlocal + ".  The last ping was recieved on " + strlp, settings.EMAIL_FROM, to)



def sendAlertEnd(project):
    #First gather addresses
    to = getAlertContacts(project)
    name = project.name

    now = datetime.utcnow()
    eastern = pytz.timezone('US/Eastern')
    local = now.replace(tzinfo=pytz.utc).astimezone(eastern)
    strlocal = local.strftime(settings.DATETIME_FORMAT)

    send_mail("Application Back Up: " + name, name + " has resumed pinning on " + strlocal, settings.EMAIL_FROM, to)
