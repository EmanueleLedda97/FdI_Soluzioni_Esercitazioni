# Acquisire da parte dell’utente 10 numeri in input. Calcolare quale sia il
# numero maggiore, e contemporaneamente contarne le occorrenze all’interno
# della sequenza digitata (ovvero contare quante volte il numero maggiore
# è stato digitato).

maggiore = 0    # Creo una variabile per il maggiore
occorrenze = 0  # Creo una variabile per contare le occorrenze del numero maggiore

# Itero il ciclo 10 volte
k = 0
while k < 10:

    num_corrente = eval(input("Digita un numero: "))  # Chiedo in input il k-esimo numero

    # Se il numero digitato è maggiore dell'attuale maggiore allora aggiorno la variabile 'maggiore'.
    # Inoltre, siccome ciò significa che è la prima volta che sto leggendo questo numero, azzero le occorrenze;
    # così facendo, l'istruzione 'if' successiva conterà correttamente il numero di occorrenze del nuovo maggiore
    if num_corrente > maggiore:
        maggiore = num_corrente     # Aggiorno il maggiore
        occorrenze = 0              # Azzero le occorrenze

    # Ogni qual volta il numero digitato è proprio uguale al numero maggiore, allora devo aumentare di uno
    # il conteggio delle occorrenze del numero maggiore
    if num_corrente == maggiore:
        occorrenze = occorrenze + 1     # Incremento occorrenze

    k = k + 1   # Incremento il contatore

# Stampo il messaggio finale in output
print("Il numero maggiore e'", maggiore, "ed e' comparso", occorrenze, "volte")
