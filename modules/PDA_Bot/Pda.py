from app.mac import mac, signals
bot=None

def set_bot(new):
    global bot
    bot=new

@signals.message_received.connect
def handle(message):
    if (bot!=None):
        bot.process_request(message)
    else:
        pass
