#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import socket
from datetime import datetime
from function import *
from reverse import *
from timer import *
from threading import Thread

class Seperation(Thread):
    def __init__(self, port1, port2, ip):
        Thread.__init__(self)
        self.portd = port1
        self.portf = port2
        self.ip = ip
    def run(self):
        scan_port(self.ip, self.portd, self.portf)

t1 = datetime.now();    
if len (sys.argv) == 2:
    ip = init_ip(sys.argv[1])
    port = 1
    port2 = 65535
    
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

else:
    usage()
dif = port2 - port
div = dif / 2
port1e = port + div
port2s = port1e + 1
port2e = port1e + div

#on creer deux thread                        
thread_1 = Seperation(port, port1e, ip)
thread_2 = Seperation(port2s, port2e,ip)

# Lancement des threads                      
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
t2 = datetime.now();
display_time_work(t1, t2)
