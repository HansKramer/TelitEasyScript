#
#  Author : Hans kramer
#
#    Date : Dec 2014
#
#    Code : trigger TER-HX910 watchdog
#

import SER

SER.set_speed('115200', '8N1')

SER.send('Hello World\r\n')

SER.send('Adios cruel world\r\n')
