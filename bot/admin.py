from django.contrib import admin

# Register your models here.

from .models import Bot, BotPlugin, Plugin


class PluginInline(admin.TabularInline):
    model = Plugin
    extra = 1


class BotPluginAdmin(admin.ModelAdmin):
    inlines = (PluginInline,)


class BotAdmin(admin.ModelAdmin):
    inlines = (PluginInline,)


admin.site.register(Bot, BotAdmin)
admin.site.register(BotPlugin, BotPluginAdmin)
