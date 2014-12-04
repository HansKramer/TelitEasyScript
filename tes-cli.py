#! /usr/bin/python
#
#    Author : Hans Kramer
#
#      Date : November 2014
#
#

from tes    import TES
from sys    import argv, exit
from getopt import getopt


optlist  = getopt(argv[1:], 'xXrlp:u:e:d:')[0]
conflict = {
    '-l' : set(('-u', 'e')),
    '-u' : set(('-l',)),
    '-e' : set(('-l',)),
}

options = {
    '-p' : "/dev/ttyS1"
}

for o in optlist:
    if conflict.has_key(o[0]) and not conflict[o[0]].isdisjoint(options.keys()):
        print "conflictng arguments %s %s" % (o[0], list(conflict[o[0]].intersection(options.keys()))[0])
        exit(-1)
    options[o[0]] = o[1]


tes = TES(port = options['-p'])

if '-l' in options:
    print tes.list()
    exit(1)

if '-u' in options:
    tes.upload(options['-u'])

if '-e' in options:
    tes.enable(options['-e'])

if '-d' in options:
    tes.delete(options['-d'])

if '-x' in options:
    tes.restart()

if '-X' in options:
    tes.restart()
    tes.read_console()


if '-r' in options:
    tes.reboot()
    
