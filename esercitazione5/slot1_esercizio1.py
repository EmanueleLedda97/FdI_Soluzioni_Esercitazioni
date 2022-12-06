# Esercizio 1: Scrivere un programma che calcoli la radice quadrata di un
# numero acquisito da tastiera, utilizzando la libreria math.

from math import *      # Con questo comando importiamo tutte le funzione della libreria math

num_digitato = eval(input("Digita un numero: "))        # Prendo in input il numero
radice = sqrt(num_digitato)                             # Calcolo la radice
print("La radice di ", num_digitato, "e'", radice)      # Stampo il valore calcolato
