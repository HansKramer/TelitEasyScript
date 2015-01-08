#
#  Author : Hans kramer
#
#    Date : Dec 2014
#
#    Code : Test the microcontroller watch dog.
#           For this to work one has to remove jumper J1 inside the module.
#

import GPIO
import SER
import time

SER.set_speed('115200', '8N1')
SER.send('Welcome at the Watchdog Test.\r\n')
SER.send('Once started and functioning you have to disable the script\r\n')
SER.send('during start-up. This can be achieved by bringing the DTR line down\r\n')
SER.send('and rebooting the system. (Note RS232 down is > 3Volt)\r\n\r\n')

#Init the HW WD
time.sleep(1)        
SER.send('Waiting for module to be fully operational\r\n')
time.sleep(10)          # wait for the module to be fully operational

SER.send('Enable the Watch Dog\r\n')
GPIO.setIOdir(8, 1, 1)  # GPIO8 in the HX910 unit is used for HW WD
time.sleep(2)
GPIO.setIOvalue(8, 0)
# Hardware watch should be enabled now.
SER.send('Hardware watch should be enabled now.\r\n')

# Start the test loop. Keep the watchdog untouched so it will kick in roughly
# after 90 seconds.
SER.send('Entering 3 minute loop.\r\n')
SER.send('Watchdog should kick in after 90 seconds or so.\r\n')
for count in range(180):
    time.sleep(1)
    SER.send('Still alive, count is at %s second(s)\r\n' % (count+1))

SER.send("It didn't work, something is wrong. Adios\r\n")
