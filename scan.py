#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import socket
from datetime import datetime
from function import *
from reverse import *
from timer import *
#from thread import *

t1 = datetime.now();    
if len (sys.argv) == 2:
    ip = init_ip(sys.argv[1])
    scan_port(ip,1,65535)
elif len (sys.argv) == 3:
    if sys.argv[1] == "-r" or sys.argv[2] == "-r":
        reversing(sys.argv)
    ip = init_ip(sys.argv[1])
    list_port = parsing_port(sys.argv[2])
    try:
        port = int (list_port[0])
        port2 = int(list_port[1])
    except:
        print ("This port is not valid")
        usage()
    is_range_port(port , port2)
    if port > port2:
        tmp = port
        port = port2
        port2 = tmp
    dif = port2 - port
    scan_port(ip, port, port2)
else:
    usage()
t2 = datetime.now();
display_time_work(t1, t2)
