from django.apps import AppConfig
from . import bot_manager


class BotRunnerConfig(AppConfig):
    name = 'bot_runner'

    def ready(self):
        import sys
        if not sys.argv[1] == 'runserver':
            return
        from bot.models import Bot
        # load_all_bot()
        # Load all bot in database
        bots = Bot.objects.all()
        for bot in bots:
            bot_manager.add_bot(bot)
