#
#  Author : Hans kramer
#
#    Date : Dec 2014
#
#    Code : Test the microcontroller watch dog.
#           In this test I limit the number of reboots by three. The count is
#           stored in the file called status that lives in /sys on the modem
#           For this to work one has to remove jumper J1 inside the module.
#

import GPIO
import SER
import time
import posix
import sys

def get_status():
    with open("status", "a+") as fp:
        data = fp.readlines()
        if data == []:
            data = 0
        else:
            data = int(data[0]) + 1
    with open("status", "w") as fp:
        fp.write(str(data))
    return data
    

if __name__ == "__main__":
    SER.set_speed('115200', '8N1')
    SER.send('Welcome at the Watchdog Test.\r\n')

    try:
        count = get_status()
        if count == 3:
            SER.send("Maximum of reboots reached.\r\nIt all worked well... is not it marvelous\r\n")
            posix.unlink("status") 
            sys.exit(0)
    except Exception, value:
        SER.send("Exception error" + str(value) + "\r\n")

    #Init the HW WD
    time.sleep(1)        
    SER.send('Watchdog try : %d\r\n' % (count+1))
    SER.send('Waiting for module to be become fully operational (after boot)\r\n')
    time.sleep(20)          # wait for the module to be fully operational

    SER.send('Enable the Watch Dog\r\n')
    GPIO.setIOdir(8, 1, 1)  # GPIO8 in the HX910 unit is used for HW WD
    time.sleep(2)
    GPIO.setIOvalue(8, 0)
    # Hardware watch should be enabled now.
    SER.send('Hardware watch should be enabled now.\r\n')

    # Start the test loop. Keep the watchdog untouched so it will kick in roughly
    # after 90 seconds.
    SER.send('Entering 2 minute loop.\r\n')
    SER.send('Watchdog should kick in after 90 seconds or so.\r\n')
    for count in range(120):
        time.sleep(1)
        SER.send('Still alive, count is at %s second(s)\r\n' % (count+1))

    SER.send("It didn't work, something is wrong. Adios\r\n")
