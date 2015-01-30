# -*- coding: utf8 -*-

'''Manejador de conexiones con websockets
por el momento es un echo server
'''
import tornado.websocket
import json

from remotebot.lib.message import error

def load_message(message):
    obj = json.loads(message)

def login(message):
    return True

def authenticate(controller, message):
    if controller.authenticated or login(message):
        yield

class WSHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, *args, **kwargs):
        super(WSHandler, self).__init__(*args, **kwargs)
        self.authenticated = tornado.web.authenticated

    def on_open(self):
        self.authenticated = False

    # FIXME: Hacer asincrónico
    def on_message(self, message):
        try:
            commands = load_message(message)
        except ValueError:
            self.write_message(error('Error decoding JSON'))
            return
        #with authenticate(self, message):
        #    #self.write_message(message)
        #    if commands['target'] == 'robot':
        #        task.robot_action(message)
        self.write_message(message)
        #self.finish()
