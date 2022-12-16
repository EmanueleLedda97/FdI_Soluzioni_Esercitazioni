# Esercizio 3: Chiedere all’utente di digitare una lista, e stampare la prima metà
# della lista (suggerimento: se la lista e’ lunga ‘n’ allora occorre fare uno
# slicing da zero fino alla metà di ‘n’)

# La funzione eval permetterà di valutare la stringa inserita dall'utente e la trasformerà
# in una vera e propria stringa (questo solo se l'utente ha digitato correttamente una lista)
lista = eval(input("Digita una lista: "))
lunghezza_lista = len(lista)                                # Calcolo la lunghezza della lista con la funzione len
prima_meta_della_lista = lista[0:(lunghezza_lista // 2)]    # Faccio uno slicing fino a meta' della lista

# Infine stampo il risultato dello slicing
print(prima_meta_della_lista)
