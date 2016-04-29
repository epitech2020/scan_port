#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import socket
from function import *
from reverse import *
if len (sys.argv) == 3:

    if sys.argv[1] == "-r" or sys.argv[2] == "-r":
        reversing(sys.argv)
    ip = sys.argv[1]
    ip_ok = is_ip(ip)
    if ip_ok != True:
        try:
            data = socket.gethostbyname_ex(ip)
            ip = data[2]
        except Exception:
            print ("invalid hostname ! check this")
            sys.exit(84)

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
    while dif >= 0:
        scan_port(ip, port)
        port = port + 1
        dif = dif - 1
else:
    usage()
