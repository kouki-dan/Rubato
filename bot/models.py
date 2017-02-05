from django.db import models
from django.contrib.auth.models import User

class BotPlugin(models.Model):
    name = models.CharField(max_length=255)
    required_parameters = models.TextField()


class Bot(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    PROVIDER_CHOICES = (
        ('s', 'slack'),
    )
    provider = models.CharField(max_length=1, choices=PROVIDER_CHOICES)

    plugins = models.ManyToManyField(BotPlugin, through='Plugin')


class Plugin(models.Model):
    bot_plugin = models.ForeignKey(BotPlugin)
    bot = models.ForeignKey(Bot)
    parameters = models.TextField()

