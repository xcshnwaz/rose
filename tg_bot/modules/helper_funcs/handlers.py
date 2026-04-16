import telegram.ext as tg
from telegram import Update

CMD_STARTERS = ('/', '!')


class CustomCommandHandler(tg.CommandHandler):
    def __init__(self, command, callback, **kwargs):
        if "admin_ok" in kwargs:
            del kwargs["admin_ok"]
        super().__init__(command, callback, **kwargs)

    def check_update(self, update):
        if (isinstance(update, Update)
                and (update.message or update.edited_message and self.allow_edited)):
            message = update.message or update.edited_message

            if message.text and len(message.text) > 1:
                fst_word = message.text_html.split(None, 1)[0]
                if len(fst_word) > 1 and any(fst_word.startswith(start) for start in CMD_STARTERS):
                    command = fst_word[1:].split('@')
                    command.append(message.bot.username)  # in case the command was sent without a username
                    if self.filters is None:
                        res = True
                    elif isinstance(self.filters, list):
                        res = any(func(message) for func in self.filters)
                    else:
                        res = self.filters(message)

                    return res and (command[0].lower() in self.command
                                    and command[1].lower() == message.bot.username.lower())

            return False


# RegexHandler was removed in python-telegram-bot v20. Provide a stub so that
# the monkey-patch in tg_bot/__init__.py and any module that references
# tg.RegexHandler does not crash on import.
_RegexBase = getattr(tg, "RegexHandler", object)


class CustomRegexHandler(_RegexBase):
    def __init__(self, pattern, callback, friendly="", **kwargs):
        if _RegexBase is object:
            # v20+: RegexHandler no longer exists; nothing to initialise.
            pass
        else:
            super().__init__(pattern, callback, **kwargs)
