# -*- coding: utf-8 -*-
"""
Corrigé exercice 3b
"""
import signal

TIMEOUT = 5 # délai de rigueur

def mongestionnaire(signum,stack):
    print('Trop tard!')
    raise TimeoutError

signal.signal(signal.SIGALRM, mongestionnaire)

def input_delai():
    try:
        print ('Vous avez {} secondes pour répondre'.format(TIMEOUT))
        rep = input()
        return rep
    except TimeoutError:
        # temps dépassé
        return "Temps dépassé"
    except KeyboardInterrupt:
        # temps dépassé
        return "Ctrl-C"

# le chrono tourne
signal.alarm(TIMEOUT)
s = input_delai()
# Ne pas oublier d'arrêter le chrono pour poursuivre
signal.alarm(0)
