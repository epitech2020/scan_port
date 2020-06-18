#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
    from time import sleep
except ImportError:
    print ("this program need scapy to work")
    sys.exit(84)

def init_ip(arg):
    ip = arg
    ip_ok = is_ip(ip)
    if ip_ok != True:
        try:
            data = socket.gethostbyname_ex(ip)
            ip = data[2]
        except Exception:
            print ("invalid hostname ! check this")
            sys.exit(84)
        return(ip)
    else:
        print ("invalid hostname ! check this")
        sys.exit(84)
        
def usage():
    print ("Usage : ./scan.py [IP] [Port start-end port]")
    print ("Usage : ./scan.py [-r] [hostname]")
    sys.exit (84)
    
_number = 0

def scan_port(ip, port_s, port_e):
    sp = RandShort()
    try:
        rep,ko = sr(IP(dst=ip)/TCP(sport=sp,dport=(port_s,port_e),flags="S"),timeout=0.3,verbose=0)
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit(84)
    except socket.error, v:
        errorcode=v[0]
        print ("invalid hostname ! check this")
        sys.exit(84)
    if rep != None:
        for emis, recu in rep:
            if recu[1].flags == 0x12:
                print ("port ouvert %d :" %recu[1].sport)

def is_ip(ip):
    test = ip.split('.')
    if len (test) == 4:
        try:
            nb = [int(z) for z in test]
        except ValueError:
            return False
        if nb[0] <= 255 and nb[1] <= 255 and nb[2] <= 255 and nb[3]:
            return True
        else:
            return False
    else:
        return False

def is_range_port(port, port2):
    if (port > 65535) or (port2 > 65535):
        print ("this range of port is not valid")
        sys.exit(84)

def parsing_port(port):
    try:
        list_port = []
        port1 = int(port)
        list_port.append(port1)
        list_port.append(port1)
        return (list_port)
    except ValueError:
        list_port = port.split('-')
        if len (list_port) != 2:
            print ("this ports are not valid")
            usage()
            sys.exit(84)
        else:
            return (list_port)

