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
        welcome_text = """
Bienvenido(a) {username} al grupo Telegram de Seguridad Informática Venezuela: https://t.me/itsec_ve

Compartimos ideas relacionadas con el tema de seguridad informática.
Criptografía, privacidad, PenTest, exploits, ingeniería reversa, entre otros.

Algunos consejos y normas para empezar:

* Preséntate cuando llegues (Chévere si nos cuentas que interés tienes en la Seguridad Informática)
* Temas on-topic: recursos, herramientas, experiencias, técnicas, etc.
* Las discusiones en el grupo se rigen por el código de conducta "convenido para contribuyentes" http://contributor-covenant.org/version/1/4/es/code_of_conduct.txt
* En concreto, las bromas de contenido sexual o inapropiado no están permitidas.
* No apoyamos el uso de estas herramientas y conocimientos para fines que estén por fuera del marco de la ley.
* Este grupo está moderado, sé respetuoso y tolerante con los demás
* "We are all consenting adults here"
        """.format(
            username='@' + username if username != '' else '',
        )

        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=welcome_text
        )