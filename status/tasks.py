from __future__ import absolute_import
from celery import shared_task

from status.updateProject import updateProjects

@shared_task
def runUpdate():
    updateProjects()
