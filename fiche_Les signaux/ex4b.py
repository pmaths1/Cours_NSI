# -*- coding: utf-8 -*-
"""
Corrigé exercice 4
"""

import threading
import time

def MyTimer(tempo = 1.0):
    threading.Timer(tempo, MyTimer, [tempo]).start()
    ## verification de la proprete du timer
    print(time.perf_counter())
    ## Reste du traitement

a = MyTimer(2.0)
a.start()
time.sleep(5.5)
a.stop()