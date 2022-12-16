# Esercizio 2: Scrivere una funzione che sposti tutti gli elementi di una lista
# nella cella adiacente successiva (e che sposti l’ultimo elemento in prima posizione).
# Esempio: Per l’input [3,9,7,1] la funzione dovrà modificare i valori della lista in [1,3,9,7]


# Logica della soluzione, esempio:
#
# Lista originale
# [1, 2, 3, 4, 5, 6]
#
# Lista divisa in due parti, da una parte l'utimo elemento, gli altri dall'altra
# [1, 2, 3, 4, 5] + [6]
#
# Se inverto le due liste ottengo la lista spostata verso destra
# [6] + [1, 2, 3, 4, 5]
# [6, 1, 2, 3, 4, 5]

def sposta_a_destra(L):

    # Calcolo l'indice dell'ultimo elemento
    ultimo_indice = len(L) - 1

    # Creo una lista contenente solo l'ultimo elemento della lista
    sottolista_ultimo_elemento = [L[-1]]

    # Creo una lista contenente tutti i primi elementi tranne l'ultimo
    sottolista_primi_elementi_meno_l_ultimo = L[:ultimo_indice]

    # La lista spostata sarà uguale alla lista composta dall'ultimo elemento all'inizio
    # seguito dai primi elementi, che risulteranno tutti spostati di uno
    lista_spostata = sottolista_ultimo_elemento + sottolista_primi_elementi_meno_l_ultimo

    # Restituisco la lista spostata
    return lista_spostata

