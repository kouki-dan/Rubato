
from .bot_manager import BotManager

import os
if "RUN_MAIN" in os.environ:
    bot_manager = BotManager()
