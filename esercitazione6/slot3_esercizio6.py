# Esercizio 6: Scrivere la funzione intersezione che prende in ingresso
# due liste contenenti numeri e restituisca una nuova lista ottenuta come
# intersezione dei loro elementi.

# La logica è la seguente: controllo TUTTI gli elementi di UNA sola lista.
# man mano, se un elemento è compreso anche nell'altra lista, allora questo farà
# parte dell'intersezione: in tal caso controllo che tale elemento non sia GIA'
# presente nella variabile che utilizzo per salvarmi gli elementi intersecati,
# e se non è presente l'aggiungo alla lista.
# Non mi serve fare due for poiché tutti gli elementi "non controllati" che esistono
# nella lista2 ma non nella lista1 non saranno presenti nell'intersezione.

# Definisco la funzione intersezione
def intersezione(lista1, lista2):
    intersezione_liste = []     # Inizialmente l'insieme non contiene elementi

    # Itero per tutti gli elementi di una delle due liste
    for e in lista1:
        # Se l'elemento è presente anche nell'altra lista E se non è già presente nella lista
        # degli elementi intersecati, allora lo aggiungo alla lista degli elementi intersecati.
        if e in lista2 and e not in intersezione_liste:
            intersezione_liste = intersezione_liste + [e]

    # Restituisco la lista degli elementi intersecati
    return intersezione_liste
