from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.name + " <" + self.email + ">"

class Project(models.Model):
    STATUS_CHOICES = (
    (0, 'Inactive'),
    (1, 'Online'),
    (2, 'Offline (Short)'),
    (3, 'Offline (Long)')
    )

    YES_NO = (
    (True, 'Yes'),
    (False, 'No'),
    )

    name = models.CharField(verbose_name='Project Name', max_length=255)
    alertedContacts = models.ManyToManyField(Contact, verbose_name='Emails to send alerts to', help_text='Note: you will automatically recieve an email, no need to add your email here.    ')
    alertAfter_s = models.IntegerField(default=60, verbose_name='Send alert after (in seconds)', help_text = 'It is reccomended that you set this slightly longer than the interval you plan on pinging. e.g. If you plan on sending a ping every 60 seconds, set this to 65.')
    active = models.BooleanField(default=False, choices=YES_NO, verbose_name='Active?', help_text='Leave this as "No" until you start pinging this system')
    url = models.SlugField(verbose_name='URL', unique=True, help_text="The url that your application sends pings to will be /ping/[this field]")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, verbose_name='Status', editable=False)
    notified = models.BooleanField(default=False, choices=YES_NO, verbose_name='Admins Notified?', editable=False)
    lastPing = models.DateTimeField(null=True, verbose_name='Last ping recieved', editable=False)
    lastPingIP = models.GenericIPAddressField(null=True, editable=False)
    created_at = models.DateTimeField("Created On", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Last Updated On",  auto_now=True, editable=False)

    def __str__(self):
        return self.name
