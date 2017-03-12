#!/usr/bin/env python2.7 
# -*- coding: utf-8 -*-  

from threading import Thread
import sys

class Seperation(Thread):
    def __init__(self, port1, port2):
        Thread.__init__(self)
        self.portd = port
        self.portf = port
    def run(self):
        sys.stdout.write("ok")
