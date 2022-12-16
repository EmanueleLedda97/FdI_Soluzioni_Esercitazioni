# Esercizio 1: Scrivere una funzione che raddoppi tutti i valori contenuti in una lista di numeri interi.


def raddoppia(L):
    # Itero sugli indici della lista
    k = 0
    while k < len(L):
        L[k] = L[k] * 2     # L'elemento k-esimo viene raddoppiato
        k = k + 1           # Incremento il contatore