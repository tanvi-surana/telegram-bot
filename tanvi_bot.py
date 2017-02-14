import time
import random
import datetime
import telepot

"""
After **inserting token** in the source code, run it:
```
This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/question':
    	bot.sendMessage(chat_id)    

bot = telepot.Bot('275495631:AAGBwM9jBjK571E1FAQPttGf-pJRLhonXh0')
bot.message_loop(handle)
print ('I am listening ...')

while 1:
	time.sleep(10)