
import time
from collections import defaultdict

from .slackclient import SlackClient


class BotManager:

    def __init__(self):
        self.bots = {}
        self.plugins = defaultdict(list)
        self.started = False

    def add_bot(self, bot):
        id_ = bot.id
        token = bot.token

        for plugin in bot.plugins.all():
            self.plugins[id_].append(plugin)

        if id_ in self.bots:
            self.stop_bot(id_)
        self.start_bot(id_, token)

    def stop_bot(self, bot_id):
        self.bots[bot_id].close()
        del self.bots[bot_id]

    def start_bot(self, id_, token):
        self.bots[id_] = SlackClient(token)
        if not self.started:
            self.started = True
            import threading
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()

    def worker(self):
        while True:
            for id_, slack_client in self.bots.items():
                events = slack_client.rtm_read()
                for event in events:
                    if event.get('type') != 'message':
                        continue
                    self._on_new_message(event, slack_client, id_)
            time.sleep(1)

    def _on_new_message(self, msg, slack_client, id_):
        subtype = msg.get('subtype', '')
        if not subtype == '':
            return
        if slack_client.id == msg['user']:
            return

        is_mention = "<@"+slack_client.id+">" in msg['text']

        if is_mention:
            self.dispatch_respond(id_, msg['text'], msg['channel'], slack_client)
        else:
            self.dispatch_listen(id_, msg['text'], msg['channel'], slack_client)

    def dispatch_respond(self, id_, text, channel, slack_client):
        for plugin in self.plugins[id_]:
            context = plugin.context

            def response(text):
                slack_client.send_message(channel, text)

            try:
                exec(context + "\nrespond_to(text)", {'text': text, 'slack': slack_client, 'response': response})
            except:
                pass

    def dispatch_listen(self, id_, text, channel, slack_client):
        for plugin in self.plugins[id_]:
            context = plugin.context

            def response(text):
                slack_client.send_message(channel, text)
                
            try:
                exec(context + "\nlisten_to(text)", {'text': text, 'slack': slack_client, 'response': response})
            except:
                pass
