# Chiedere all’utente di digitare un numero intero ‘n’, e dopodiché
# stampare tutti i numeri tra 0 ed n.

n = eval(input("Digita un numero: "))   # Chiedo l'input all'utente

k = 0   # Inizializzo il contatore a zero, in quanto devo stampare i numeri da 0 ad n

# Ripeto la sequenza di istruzioni finché k NON sarà maggiore di n (quindi finché k <= n)
while k <= n:
    print(k)    # Stampo il valore corrente
    k = k + 1   # Incremento il contatore
