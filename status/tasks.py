from __future__ import absolute_import

from status.updateProject import updateProjects
from celery import shared_task

@shared_task
def runUpdate():
    updateProjects()
