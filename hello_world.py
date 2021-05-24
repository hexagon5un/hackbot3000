import socket
import time
import os
import random
import re

## IRC Config
server = "irc.libera.chat" 
port = 6667
channel = "#hackaday-bots"

botnick = "hackbot3000"
realname = "Botty McBotface" ## shows up when someone WHOs you. Say you're a bot?

REGISTERED = True  ## log in on the bot account, register it.
botpassword = "bad_password_changeme"

DEBUG = True


## Functions
def receive(numBytes = 1024):
    return irc.recv(numBytes).decode("UTF-8")

def send(msg):
    irc.send(bytes(msg + "\n", "UTF-8"))

def say(msg, dest=channel):
    """Sends a message, default to the registered channel,
        but you can write to other channels and/or direct message users too.
        IRC client equiv: /msg """
    send("PRIVMSG {} :{}".format(dest, msg))

def parse(msg):
    if " PRIVMSG " in msg:
        nickre = re.compile('^:(.*)!(.*) PRIVMSG (.*) :(.*)$')
        parsed = dict(zip(["nick","user","to","message"],
            nickre.findall(msg)[0]))
    else: 
        ## Todo: Handle other message types here if it matters
        pass
    return(parsed)

## Connect and Login

irc = socket.socket()
irc.connect((server, port))

send("NICK {}".format(botnick))
send("USER {} 0 * :{}".format(botnick, realname))
if REGISTERED:
    # /msg NickServ identify your_password_here
    say("identify {}".format(botpassword), "NickServ")

time.sleep(5)
send("JOIN {}".format(channel))


## Endless Event loop.  
while True:
    text = receive().strip()  ## blocking, waits for message
    if DEBUG:
        print(text)

    ## Handle ping/pong keepalive
    if text.startswith("PING"): 
        pingserver = text.split()[1]
        send('PONG {}'.format(pingserver))

    ## Handle "normal" messages
    if " PRIVMSG " in text:  
        parsed = parse(text)
        ## channel message
        if parsed["to"] == channel: 
            if botnick in parsed["message"]: ## talking about/to me?
                if "hello" in parsed["message"]:
                    say( "Hello {}".format(parsed["nick"]) ) 
                if "mama" in parsed["message"]:
                    say("Don't you talk about my mama!")
        ## personal message 
        if parsed["to"] == botnick:  
            if parsed["message"] == "shutdown":
                say("Goodbye!")
                break
            else:
                ## loopback test: reply with personal message
                say(parsed["message"], parsed["nick"])

## Cleanup
send('PART {}'.format(channel))
send('QUIT :{}'.format("I'm done."))
irc.close()

