#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
import sys
def hostname_to_ip(host):
    try:
        data = socket.gethostbyname_ex(host)
        ip = data[2]
        return (ip)
    except Exception:
        print ("invalid hostname ! check this")
        sys.exit(84)
                
def reversing(argument):
    if argument[1] == "-r":
        ip = hostname_to_ip(argument[2])
    else:
        ip = hostname_to_ip(argument[1])
    print ("target [IP] is -> %s" %ip)
    sys.exit(0)
