# Esercizio 6: Scrivere una funzione che prenda in ingresso un numero
# ‘n’ e ne restituisca il fattoriale.

#   Nome: fattoriale
#
#   Argomenti:
#       - n: numero di cui vogliamo calcolare il fattoriale
#
#   Valore di ritorno: fattoriale di 'n'
def fattoriale(n):
    fatt = 1
    k = 2
    while k <= n:
        fatt = fatt * k
        k = k + 1
    return fatt

fattoriale(3)
