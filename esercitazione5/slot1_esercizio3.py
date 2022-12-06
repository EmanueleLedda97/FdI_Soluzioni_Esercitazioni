# Esercizio 3: Scrivere un programma che acquisisca il raggio di un
# cerchio e ne calcoli l’area (usando le variabili della libreria math).

from math import *

raggio = eval(input("Digita il raggio: "))      # Prendo in input il raggio
area = pi * (raggio ** 2)                       # Calcolo l'area usando la variabile della libreria math
print(area)                                     # Stampo l'area
