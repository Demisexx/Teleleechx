from tobrot import LOGGER, BOT_LANG
from tobrot.bot_theme.languages import en, bn

AVAILABLE_LANG = {'english': en, 'bengali': bn}

def BotLang():

    if BOT_LANG in AVAILABLE_LANG.keys():
        return (AVAILABLE_LANG.get(BOT_LANG)).TXLanguage()
    else:
        return en.TXLanguage()
