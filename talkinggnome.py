#!/usr/bin/env python3
#MAKE SURE IT'S PYTHON 333333333!

# This is a Raspberry Pi program for the talking gnome.
# The requirement is to connect to the talesofthepark website via a websocket and use text to speech
# on the messages going between the users and gnomes in real-time.
#
# Does what it says on the tin, it's a talking gnome...
#
# Socket: ws://talesofthepark.com/talking/fred/
# Test Page: http://talesofthepark.com/talking/fred/
# fred is the name of the gnome, so you can listen to a specific one, or use 'all' to listen to all of them.

#https://github.com/websocket-client/websocket-client

#json response looks like this:
#{
#   "name": "Visitor",
#   "gnomename": "fred",
#   "timestamp": "2017-10-02 12:08:27",
#   "isgnome": false,
#   "visitorname": "Visitor",
#   "message": "hello again fred did you miss me"
#}

#flite command is:
#  flite -t "hello gnome"
#or
#  flite -voice xxx -t "hello gnome"
#
#festival is the other text to speech system yo could use, but
#they're largely similar

import os
import time
import json
import argparse
import websocket
#import thread

#configuration - address of the web service to hook into
#addr = "ws://talesofthepark.com/talking/fred/"
addr = "ws://128.40.47.88:8000/talking/fred/"
#does this work as an echo? ws://echo.websocket.org/


def on_message(ws, message):
    #print(message)
    jframe = json.loads(message)
    speakingname = jframe["name"] #name of who actually spoke message
    text = speakingname + " says, " + jframe["message"]
    print("say: ",jframe["message"])
    #todo: need to sanitise text for quotes
    cmd = 'flite -t "{0}"'.format(text)
    print("cmd: ",cmd)
    os.system(cmd)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("open")

def main():
    print("talking gnome.py running...")

    #todo: add some options here i.e. what gnome do you want to listen to?
    #parser = argparse.ArgumentParser(description='A talking gnome')
    #parser.add_argument('--gnome', help='name of the gnome')
    #args = parser.parse_args()
    #print(args)


    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(addr,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

###############################################################################
if __name__ == "__main__":
    main()
