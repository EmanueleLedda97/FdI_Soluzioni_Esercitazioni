# Esercizio 3: Scrivere una funzione che prende in ingresso una lista e ne azzeri gli elementi negativi.

def azzera_negativi(L):
    k = 0
    while k < len(L):
        # Se l'elemento k-esimo è negativo allora lo azzero
        if L[k] < 0:
            L[k] = 0
        k = k + 1

