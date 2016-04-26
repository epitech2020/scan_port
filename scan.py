#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

def scan_port(ip, port):
    sp = RandShort()
    rep = sr1(IP(dst=ip)/TCP(sport=sp,dport=port,flags="S"),timeout=0.3,verbose=0)
    if rep != None:
        if TCP in rep:
            if rep[TCP].flags == 0x12:
                print ("Le port %d est ouvert" %port)
            elif rep[TCP].flags == 0x14:
                print ("Le port %d est fermé" %port)
    else:
        print ("Impossible de joindre l'IP %s" %ip)
        sys.exit (-84)
        
def check_port(port):
    port = str(port)
    lengt = len (port)
    i = 0;
    while i < lengt:
        if port[i] == '-':
            return 1
        i+=1
    return 0
    
if len (sys.argv) == 4:
    ip = sys.argv[1]
    port = int (sys.argv[2])
    port2 = int(sys.argv[3])

    #a = check_port(port)
    #print("le retour vaux %d" % a)
    
    dif = port2 - port
    while dif >= 0:
        scan_port(ip, port)
        port = port + 1
        dif = dif - 1
else:
    print ("Usage : ./scan.py [IP] [start port] [end port]")
