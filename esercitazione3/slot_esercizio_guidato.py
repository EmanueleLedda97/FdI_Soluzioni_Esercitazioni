# Scrivere, mediante l’utilizzo di un ciclo while, un programma che stampi i
# primi 5 numeri interi. Dopo aver stampato i numeri, il programma deve
# stampare la stringa “Fine del programma”

# Creo la variabile contatore 'k' che parte da 1, che verrà utilizzata per iterare
# un ciclo 5 volte. Viene inizializzata col valore 1 poiché voglio stampare il valore 1
# come primo valore.
k = 1

# Creo un ciclo while che si fermerà solo quando il valore k sarà minore o uguale a 5.
# In questo modo, grazie all'istruzione k = k + 1 dentro al while, k verrà incrementato
# progressivamente fino a diventare maggiore stretto di 5, permettendomi di uscire dal ciclo.
while k <= 5:
    # Siccome k è il mio contatore (che sto incrementando progressivamente con k = k + 1)
    # allora ad ogni iterazione esso assumerà proprio il valore che ci è stato richiesto di
    # stampare, ovvero un numero intero; siccome il ciclo sarà eseguito 5 volte, stamperà
    # proprio i primi 5 numeri interi (come richiesto dalla consegna)
    print(k)

    # Qui incremento "di uno" k, ovvero "aggiungo 1" al valore attuale di k.
    k = k + 1

# Alla fine del programma, quindi fuori dal while, stampo la stringa "Fine del programma"
print("Fine del programma")


# N.B. ci sono tanti modi per risolvere questo tipo di esercizi, qui ad esempio abbiamo fatto
# partire il contatore da 1 ed iterato per k <= 5, ma possiamo "iterare cinque volte" in tanti modi,
# anche facendo partire da 0 e usando come condizione k < 5. è importante però notare che se utilizziamo
# la notazione partendo da 0, se usiamo print(k) non otterremo in output 1,2,3,4,5 ma otterremo 0,1,2,3,4.
# Per risolvere questo problema possiamo stampare il successivo di k, quindi k+1.
#
# Soluzione alternativa:
# k = 0
# while k < 5:
#     print(k + 1)
#     k = k + 1
# print("Fine del programma")
