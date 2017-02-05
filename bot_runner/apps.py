from django.apps import AppConfig
from . import bot_manager

class BotRunnerConfig(AppConfig):
    name = 'bot_runner'

    def ready(self):
        import sys
        if not sys.argv[1] == 'runserver':
            return
        import os
        if not "RUN_MAIN" in os.environ:
            return
        from bot.models import Bot
        # Load all bot in database
        bots = Bot.objects.all()
        for bot in bots:
            bot_manager.add_bot(bot)
