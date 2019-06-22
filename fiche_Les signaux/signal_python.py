#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:39:28 2019

@author: Pascal Malingrey
"""

from time import sleep


try:
    print ("C'est parti'")
    i = 0
    while True:
        i += 1
        print ("Iteration #{}".format(i))
        sleep(1)
except KeyboardInterrupt:
    # Le signal est detecte
    print("Vous essayez d'interrompre le programme")
finally:
    print ("Au revoir ")
