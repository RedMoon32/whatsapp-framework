from app.mac import mac, signals
bot=None

def set_bot(new):
    global bot
    bot=new

@signals.message_received.connect
def pda(message):
    if (bot!=None):
        bot.process_request(message)
    else:
        pass