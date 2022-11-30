# Scrivere un programma che chieda all’utente di digitare un numero ‘n’;
# dopodiché chiedere all’utente di digitare ‘n’ numeri. Dopo aver digitato
# i numeri, il programma dovrà determinare se il numero ‘n’ è stato digitato
# nella sequenza di numeri digitati, e stampare “il numero n è stato digitato”
# oppure “il numero n non è stato digitato”.

# Prendo in input un numero n
n = eval(input("Digita il primo numero: "))

# Messaggio opzionale: stampo un recap delle operazioni che verranno richieste
print("Hai digitato", n, "quindi verrà cercato", n, "in una sequenza di", n, "numeri.")

# Creo una variabile per tenere traccia della ricerca del numero 'n' durante il ciclo
numero_trovato = False
i = 0
while i < n:
    # Prendo in input un numero
    numero_corrente = eval(input("Digita un numero: "))

    # Se il numero digitato è proprio 'n' allora il numero è presente nella sequenza...
    if numero_corrente == n:
        numero_trovato = True   # ... quindi segno a True il valore della variabile 'numero_trovato'

    # Incremento il contatore
    i = i + 1

# Stampo l'esito della ricerca
if numero_trovato:
    print("Il numero", n, "e' presente nella sequenza")
else:
    print("Il numero", n, "non e' presente nella sequenza")