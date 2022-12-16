# Esercizio 1: Scrivere un programma che stampi l’esito del lancio di un dado a sei facce.

# Importo la funzione randint dalla libreria
from random import randint

# Genero un numero intero casuale tra 1 e 6
lancio = randint(1, 6)

# Stampo l'esito del numero casuale
print("Lancio del dado... E' uscito ", lancio)
