import signal

TIMEOUT = 5 # délai de rigueur
CPT =1

def mongestionnaire(signum,stack):
    global CPT
    if CPT == 1:
        print("Je suis généreux, je vous laisse encore 5 secondes")
        CPT += 1
        signal.alarm(TIMEOUT)
    else:
        print('Trop tard!')
        raise TimeoutError

signal.signal(signal.SIGALRM, mongestionnaire)

def input_delai():
    try:
        print ('Vous avez {} secondes pour répondre'.format(TIMEOUT))
        rep = input()
        return rep
    except TimeoutError: # temps dépassé
        return "temps depassé"

# le chrono tourne
signal.alarm(TIMEOUT)
s = input_delai()
# Ne pas oublier d'arrêter le chrono pour poursuivre
signal.alarm(0)
print( 'votre réponse est:',s)