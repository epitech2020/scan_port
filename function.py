#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
except ImportError:
    print ("this program need scappy for work")
    sys.exit(84)


def usage():
    print ("Usage : ./scan.py [IP] [Port start-end port]")
    print ("Usage : ./scan.py [-r] [hostname]")
    sys.exit (84)

def scan_port(ip, port_s, port_e):
    sp = RandShort()
    compt = port_s
    try:
        rep = sr1(IP(dst=ip)/TCP(sport=sp,dport=(port_s, port_e),flags="S"),timeout=0.3,verbose=0)
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit(84)
    except socket.error, v:
        errorcode=v[0]
        if errorcode== 1:
            print ("you must launch this tool with rights root")
        else:
            print ("invalid hostname ! check this")
        sys.exit(84)
    if rep != None:
        if TCP in rep:
            if rep[TCP].flags == 0x12:
                print ("%s the port %d is open" %(ip, compt))
            #elif rep[TCP].flags == 0x14:
                #print ("%s the port %d is close" %( ip, port))
    else:
        print ("%s is unavaiable" %ip)
    compt += 1

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
            print ("ports not valid")
            usage()
            sys.exit(84)
        else:
            return (list_port)

