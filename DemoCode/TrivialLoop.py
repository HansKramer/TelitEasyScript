#
#  Author : Hans kramer
#
#    Date : Dec 2014
#
#    Code : Trivial Loop
#

import SER
import time

SER.set_speed('115200', '8N1')

for i in range(60):
    SER.send('Hello World %d\r\n' % i)
    time.sleep(1)

SER.send('Adios cruel world\r\n')
