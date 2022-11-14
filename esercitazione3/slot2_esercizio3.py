# Acquisire in input un numero naturale ‘n’, calcolare il valore del
# fattoriale di ‘n’ e stamparne il valore. Ricordiamo che la formula
# del fattoriale viene espressa in questo modo:
#   n! = n * (n-1)!
#   0! = 1

n = eval(input("Digita un numero: "))   # Chiedo l'input all'utente

fattoriale = 1  # Inizializzo il fattoriale ad 1, in quanto fattoriale di 0 è uguale ad 1

# Iteriamo da 1 ad n compreso
# N.B. possiamo far partire k da 1 o da 2, tanto il risultato è indifferente ai fini del fattoriale.
# L'importante è non farlo partire da zero, in quanto creerebbe una moltiplicazione per zero (azzerando
# il valore del fattoriale)
k = 1
while k <= n:
    fattoriale = fattoriale * k     # Moltiplico per il k-esimo elemento
    k = k + 1                       # Incremento il contatore

# Stampo infine il valore del fattoriale
print("Il fattoriale di ", n, "e'", fattoriale)
