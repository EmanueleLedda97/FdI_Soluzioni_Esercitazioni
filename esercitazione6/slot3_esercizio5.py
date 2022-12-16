# Esercizio 5: Scrivere un programma che chieda all'utente di inserire
# una sequenza di numeri (dopo averne chiesto la lunghezza), li memorizzi
# in una lista e dopo averne calcolato la somma e la media stampi il
# risultato sulla shell.

# SOLUZIONE POSSIBILE: Per comodità, siccome il programma mi chiedere prima di tutto
# di creare una lista di elementi digitati dall'utente, mi creo una funzione per
# svolgere questo compito. In questo modo mi basterà richiamare la funzione
# per creare la lista.

# Definisco la funzione per creare una lista lunga n_elementi
def crea_lista(n_elementi):
    lista = []      # Creo una lista inizialmente vuota
    k = 0           # Inizializzo a zero il contatore

    while k < n_elementi:
        numero_corrente = eval(input("Digita un numero: "))     # Prendo in input il numero corrente...
        lista = lista + [numero_corrente]                       # ... e lo concateno alla lista

    return lista    # Infine restituisco la lista creata

# Prendo in input la lunghezza della lista e creo una lista con quella lunghezza
lunghezza_lista = eval(input("Digita la lunghezza della lista: "))
la_mia_lista = crea_lista(lunghezza_lista)

# Effettuo una somma cumulativa sugli elementi della lista
somma = 0
for el in la_mia_lista:
    somma = somma + el

# Calcolo la media sulla lista
media = somma / lunghezza_lista

# Stampo il risultato
print("La somma degli elementi e'", somma, "mentre la media e'", media)

