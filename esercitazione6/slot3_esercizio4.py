# Esercizio 4: Scrivere un programma che consenta all’utente di costruire la lista
# della spesa. Il programma dovrà chiedere all'utente di inserire la descrizione
# di ciascun prodotto da acquistare (sotto forma di una stringa), e
# dovrà memorizzarlo in una lista. Dopo l'inserimento di ogni prodotto
# il programma dovrà chiedere all’utente se vuole inserirne un altro.
# Al termine il programma dovrà stampare nella shell la lista della spesa.

lista_della_spesa = []      # Creo la lista inizialmente vuota
scelta = 's'                # Imposto una scelta iniziale ad 's' per indicare la volontà di inserire un prodotto

# Continuo ad iterare fintanto che l'utente dice di voler digitare un altro prodotto (digitando 's')
while scelta == 's':
    prodotto_corrente = input("Digita un prodotto da comprare")     # Prendo in input un prodotto
    lista_della_spesa = lista_della_spesa + [prodotto_corrente]     # Aggiungo il prodotto alla lista della spesa

    # Chiedo all'utente se vuole aggiungere un nuovo prodotto
    scelta = input("Vuoi digitare un altro prodotto? (s/n): ")

# Infine stampo la lista della spesa
print("La tua lista della spesa contiene i seguenti prodotti: ", lista_della_spesa)