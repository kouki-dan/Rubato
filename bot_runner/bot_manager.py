
from .slackclient import SlackClient


class BotManager:

    def __init__(self):
        self.bots = {}

    def add_bot(self, bot):
        id_ = bot.id
        token = bot.token

        if id_ in self.bots:
            self.stop_bot(id_)
        self.start_bot(id_, token)

    def stop_bot(self, bot_id):
        pass

    def start_bot(self, id_, token):
        self.bots[id_] = SlackClient(token)
