import signal
import time

def mongestionnaire(sig,frame):
	if sig == signal.SIGINT:
		print("Ctrl-C est désactivé")

signal.signal(signal.SIGINT, mongestionnaire)

i = 1
while 1:
	print("itération :{}".format(i))
	time.sleep(1)
	i += 1
