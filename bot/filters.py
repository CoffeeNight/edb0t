from telegram.ext import BaseFilter


class NewChatMemberFilter(BaseFilter):
    def filter(self, message):
        return bool(message.new_chat_member)