from telegram.ext import MessageHandler

from bot.filters import NewChatMemberFilter


class Handlers(object):
    """
    Contains the all the bot handlers for specific events triggered.

    """
    def __init__(self, dispatcher):
        """
        :param dispatcher: Dispatcher instance to initialize the handlers
        """
        self.dispatcher = dispatcher

    def init_handlers(self):
        new_member_handler = MessageHandler(
            NewChatMemberFilter(), self.new_member)
        self.dispatcher.add_handler(new_member_handler)

    def new_member(self, bot, update):
        username = update.message.new_chat_member.username
        welcome_text = 'Hola {username}!'.format(
            username='@' + username if username != '' else '',
        )

        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=welcome_text
        )
