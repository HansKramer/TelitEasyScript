#
#  Author : Hans kramer
#
#    Date : Dec 2014
#
#    Code : SMS 
#

import SER
import MDM
import time


if __name__ == "__main__":
    SER.set_speed('115200', '8N1')

    recipient = "Your Phone"
    message   = "Your message here"

    MDM.send('ATE0\r\n', 10)
    MDM.send('ATZ\r\n', 10)
    MDM.send('AT+CMGF=1\r\n', 10)
    MDM.send('AT+CMGS="' + recipient + '"\r\n', 10)
    MDM.send(message + "\r\n", 10)
    MDM.send(chr(26) + "\r\n", 10)
    SER.send(data + "\r\n")

