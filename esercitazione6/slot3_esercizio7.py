# Esercizio 7: Scrivere la funzione ‘unione’ che prende in ingresso due liste
# contenenti numeri e restituisca una nuova lista ottenuta come unione dei loro
# elementi (occhio che si intende unione insiemistica, quindi gli elementi
# della lista devono essere singolari, e non ripetuti).

# Qui la logica è diversa rispetto all'intersezione: dovrò controllare
# tutti gli elementi di entrambe le liste, e man mano li dovrò aggiungere
# all'unione in modo cumulativo.
# QUINDI, per simulare lo "scorrere" di entrambe le liste concateno le due
# liste in un'unica lista e vado ad attuare un for sulla concatenazione

# Definisco la funzione
def unione(lista1, lista2):
    unione_liste = []       # Creo una lista inizialmente vuota

    # Itero per ogni elemento di entrambe le liste
    for e in lista1 + lista2:
        # Se l'elemento non è già presente nella lista dell'unione, lo aggiungo
        if e not in unione_liste:
            unione_liste = unione_liste + [e]

    # Restituisco l'unione delle due liste
    return unione_liste
