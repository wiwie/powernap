import re, commands
from logging import error, debug, info, warn, os

class FileChangeDateMonitor():

    # Initialise
    def __init__ ( self, config ):
        self._lastcheck = -1
        self._type = config['monitor']
        self._name = config["name"]
        self._regex = config['regex']
        self._absent_seconds = 0

    def start(self):
        pass

    def active(self):
        # my custom code:
        lsof = long(commands.getoutput("stat -c %%Y '%s'" % self._regex))
	result = self._lastcheck > -1 and lsof > self._lastcheck
	self._lastcheck = lsof
        return result

# ###########################################################################
# Editor directives
# ###########################################################################

# vim:sts=4:ts=4:sw=4:et
