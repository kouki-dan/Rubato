from django.db import models
from django.contrib.auth.models import User


class BotPlugin(models.Model):
    name = models.CharField(max_length=255)
    required_parameters = models.TextField()

    TYPE = (
        ('py1', 'python_simple_plugin_ver1'),
    )
    type = models.CharField(max_length=255, choices=TYPE)
    context = models.TextField()

    def __str__(self):
        return self.name

class Bot(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    token = models.CharField(max_length=255)

    PROVIDER_CHOICES = (
        ('s', 'slack'),
    )
    provider = models.CharField(max_length=1, choices=PROVIDER_CHOICES)

    plugins = models.ManyToManyField(BotPlugin, through='Plugin')

    def __str__(self):
        return self.name


class Plugin(models.Model):
    bot_plugin = models.ForeignKey(BotPlugin)
    bot = models.ForeignKey(Bot)
    parameters = models.TextField()
