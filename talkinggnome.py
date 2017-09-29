#!/usr/bin/env python3

# This is a Raspberry Pi program for the talking gnome.
# The requirement is to connect to the talesofthepark website via a websocket and use text to speech
# on the messages going between the users and gnomes in real-time.
#
# Does what it says on the tin, it's a talking gnome...
#
# Socket: ws://talesofthepark.com/talking/fred/
# Test Page: http://talesofthepark.com/talking/fred/
# fred is the name of the gnome, so you can listen to a specific one, or use 'all' to listen to all of them.

import os
import time
import json
import argparse
from websocket import create_connection, WebSocket

#configuration - address of the web service to hook into
addr = "ws://talesofthepark.com/talking/fred/"

class GnomeWebSocket(WebSocket):
    def __init__(self):
        """
        Constructor
        """
        self.enableTTSFlite=True
        self.enableTTSFestival=False
        self.voice='' #name of voice to use
        self.enableTTY=True #true and text appears on the screen
        self.ttyPrompt="Gnome says: " #text that appears before the text on the screen

    def recv_frame(self):
        frame = super().recv_frame()
        print('I got this frame: ', frame)
        return frame

    def ttsFlite(self,text):
        """Text to speech using flite"""
        cmd=''
        if self.voice=="":
            cmd = 'flite -t "{0}"'.format(text)
        else:
            cmd = 'flite -voice {0} -t "{1}"'.format(self.voice,text)
        print("command: ",cmd)
        os.system(cmd)

def main():
    print("entry point")

    #parser = argparse.ArgumentParser(description='A talking gnome')
    #parser.add_argument('--gnome', help='name of the gnome')
    #args = parser.parse_args()
    #print(args)

    ws = create_connection(addr, class_=GnomeWebSocket)
    while True:
        time.sleep(10)



###############################################################################
if __name__ == "__main__":
    main()
