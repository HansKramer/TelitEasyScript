#! /usr/bin/python
#
#    Author : Hans Kramer
#
#      Date : November 2014
#
#

import serial
import time
import syslog
import sys


class TES(serial.Serial):

    def __init__(self, port = "/dev/ttyS0"):
        #serial.Serial.__init__(self, port, 115200, parity='N', xonxoff=False, timeout=1, dsrdtr=True, rtscts=False)
        serial.Serial.__init__(self, port, 115200, parity='N', xonxoff=False, timeout=1, dsrdtr=False, rtscts=False)
        self.echo(False)
  
    def echo(self, on = True):
        self.write("ATE%d\r" % on)
                
    def read_results(self):
        result = []
        for line in self.readlines():
            if line[:-2] not in ("OK", ""):
                result.append(line[:-2])
        return result
 
    def list(self):
        self.write("AT#LSCRIPT\r")
        result = []
        for line in self.readlines():
            if line[:-2] not in ("OK", ""):
                result.append(line[:-2])
        return result

    def upload(self, filename):
        with open(filename, "r") as fp:
            script = "".join(fp.readlines())
        self.write('AT#WSCRIPT="%s",%d\r\n' % (filename, len(script)))
        print self.read_results()
        self.write(script)
        print self.read_results()

    def delete(self, filename):
        self.write('AT#DSCRIPT="%s"\r' % filename)
        print self.read_results()

    def enable(self, filename):
        self.write('AT#ESCRIPT="%s"\r\n' % filename)
        print self.read_results()

    def reboot(self):
        self.write('AT#REBOOT\r\n')

    def restart(self):
        self.write('AT#EXECSCR\r\n')

    def read_console(self):
        while True:
            for line in self.readlines():
                print line[:-2]
