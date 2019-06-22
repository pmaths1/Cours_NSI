import signal, time, sys

def mongestionnaire(signum,stack):
    print ("Arrêt du programme")
    sys.exit(0)

def inconnue(n):
    signal.signal(signal.SIGALRM,mongestionnaire)
    signal.alarm(5)
    while n>0:
        print('je travaille',n)
        time.sleep(1)
        n -= 1