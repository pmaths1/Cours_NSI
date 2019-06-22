#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:34:39 2019
@author: pascal
"""
import signal
import sys
def signal_handler(signal, frame):
        print('Vous avez appuyer Ctrl+C!')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Utilisez Ctrl+C pour terminer le programme')
signal.pause()
