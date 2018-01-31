# Coding = utf-8
# irc.py - An Utility IRC Bot

import socket
import asyncore
import asynchat


class Bot(asynchat.async_chat):
    """Low-level class that deals with the socket part of the bot, connecting, reading, etc."""
    def __init__(self):
        asynchat.async_chat.__init__(self)
        self.set_terminator(b'\n')
        self.buffer = ''
        # TODO Code this