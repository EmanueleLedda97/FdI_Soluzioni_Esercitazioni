# Esercizio 2: Scrivere un programma che stampi l’esito del lancio di una moneta (testa/croce).
from random import random


# Definisco la funzione per il lancio della moneta
def lancia_moneta():
    lancio = 'testa'
    r = random()    # Genero un numero random tra 0 e 1

    # Come logica impongo l'esito del numero maggiore di 0.5, in quanto l'eventualità di avere
    # un esito maggiore o minore di 0.5 è equiprobabile (50%, come per il lancio di una moneta)
    if r > 0.5:
        lancio = 'croce'

    # Restituisco l'esito del lancio
    return lancio


# Simulo e stampo il lancio di una moneta
il_mio_lancio_di_moneta = lancia_moneta()
print("E' uscito ", il_mio_lancio_di_moneta)
