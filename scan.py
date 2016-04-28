#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import socket
try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
except ImportError:
    print ("this program need scappy for work")
    sys.exit(-84)
    
################ Function scan #############

def scan_port(ip, port):
    sp = RandShort()
    try:
        rep = sr1(IP(dst=ip)/TCP(sport=sp,dport=port,flags="S"),timeout=0.3,verbose=0)
    except socket.error, v:
        errorcode=v[0]
        if errorcode== 1:
            print ("you must launch this tool with rights root")            
        else:
            print ("invalid hostname ! check this")
        sys.exit(-84)
    if rep != None:
        if TCP in rep:
            if rep[TCP].flags == 0x12:
                print ("the port %d is open" %port)
            elif rep[TCP].flags == 0x14:
                print ("the port %d is close" %port)
    else:
        print ("%s is unavaiable" %ip)

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
        sys.exit(-84)

if len (sys.argv) == 4:
    ip = sys.argv[1]
    ip_ok = is_ip(ip)
    if ip_ok != True:
        try:
            data = socket.gethostbyname_ex(ip)
            ip = data[2]
        except Exception:
            print ("invalid hostname ! check this")
            sys.exit(-84)
    try:
        port = int (sys.argv[2])
        port2 = int(sys.argv[3])
    except:
        print ("This port is not valid")
        print ("Usage : ./scan.py [IP] [start port] [end port]")
        sys.exit(-84)
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
    print ("Usage : ./scan.py [IP] [start port] [end port]")
    sys.exit (-84)
