# Chiedere all’utente di digitare un numero e stamparne la scomposizione
# in fattori primi. Esempio: se l’utente digita 12 il programma dovrà
# stampare in sequenza i numeri “2”, “2”, “3”. Altro esempio: Se l’utente
# digita il numero 30 il programma dovrà stampare in sequenza i numeri
# “2”, “3”, “5”.

# Prendo in input il numero da fattorizzare
numero_da_scomporre = eval(input("Digita un numero da fattorizzare: "))

# Riga opzionale: per preservare il valore della variabile di sopra me ne creo una
# nuova che andrò a modificare dentro al while.
scomposizione = numero_da_scomporre

# Divido iterativamente (mediante divisione tra interi) il numero digitato fino
# ad ottenere il numero 1.
divisore = 2
while scomposizione > 1:
    # Se il numero e' divisibile per il divisore allora il divisore e' uno dei fattori, quindi lo stampo
    # e divido il numero da scomporre
    if scomposizione % divisore == 0:
        print(divisore)
        scomposizione = scomposizione // divisore
    # Altrimenti significa che il divisore non è tra i fattori, quindi lo incremento
    else:
        divisore = divisore + 1
