# Scrivere un programma che chieda all'utente di inserire un numero intero
# positivo ‘n’, e che crei una stringa di lunghezza ‘n’ composta
# dall’alternanza dei caratteri ‘a’ e ‘b’; stampare infine la stringa.
# Esempio: se l’utente digita 5 il programma dovrà creare la stringa “ababa”
# e stamparla.

# Prendo in input il valore 'n'
n = eval(input("Digita un numero: "))

# Creo una variabile per contenere la squenza di caratteri, inizialmente vuota
sequenza = ""

# Creo una variabile contatore per iterare il ciclo while fino ad 'n' iterazioni
i = 0
while i < n:
    # Se il contatore ha indice pari aggiungo una 'a' alla sequenza...
    if i % 2 == 0:
        sequenza = sequenza + 'a'
    # ... altrimenti aggiungo una 'b' alla sequenza
    else:
        sequenza = sequenza + 'b'

    # Incremento il contatore del ciclo
    i = i + 1

# Infine stampo in output la sequenza prodotta
print(sequenza)
