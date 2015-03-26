'''
Base class for the entities supported by XRemoteBot
'''
import logging

logger = logging.getLogger('remotebot')

class Entity(object):
    def _send(self, method, wshandler, msg_id, *args, **kwargs):
        logger.debug('Calling %s.%s with args %s', self.__class__, method, (args, kwargs))
        return getattr(self, method)(wshandler, msg_id, *args, **kwargs)
