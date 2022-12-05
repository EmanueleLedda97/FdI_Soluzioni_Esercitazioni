# Chiedere all’utente di digitare un numero intero ‘n’, e calcolare la somma
# dei primi n numeri naturali; dopodiché stampare tale valore.

# Creo una variabile che conterrà la somma dei primi numeri naturali: faccio partire
# la variabile da zero e la utilizzerò per sommare cumulativamente la variabile.
somma = 0

n = eval(input("Digita un numero: "))   # Chiedo l'input all'utente
k = 1   # Voglio iterare n volte, parto da zero e impongo nel ciclo k<n
while k <= n:
    # Ad ogni iterazione k assumerà il valore del k-esimo numero naturale; quindi, se noi
    # sommiamo cumulativamente tutti i k da 0 ad n noi otteniamo la somma di tutti i primi
    # n numeri naturali.
    somma = somma + k
    k = k + 1   # Incremento di uno poiché voglio scorrere uno a uno tutti i numeri naturali

print("Il valore della somma e'", somma)
