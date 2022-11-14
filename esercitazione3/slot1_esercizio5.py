# Chiedere all’utente di digitare un numero intero ‘n’. Dopodiché, acquisire
# dall’utente ‘n’ numeri interi, calcolarne la media aritmetica e stamparne
# il valore.

# Soluzione: la media aritmetica di n numeri si calcola come
#   (x1+x2+x3+...+xn) / n
# quindi, a noi basta ottenere il numeratore (x1+x2+x3+...+xn) attraverso una somma cumulativa,
# e successivamente ottenere la media come somma/n


n = eval(input("Di quanti numeri vuoi fare la media? "))   # Chiedo l'input all'utente

somma = 0   # Faccio partire la somma cumulativa da zero
k = 0       # Impongo k=0 e come condizione k<n per iterare n volte
while k < n:
    num_corrente = eval(input("Digita un numero: "))    # Chiedo in input il k-esimo numero
    somma = somma + num_corrente    # Sommo cumulativamente i numeri digitati
    k = k + 1                       # Incremento k di uno

# Calcolo e stampo in output la media aritmetica
media = somma / n
print("La media aritmetica e'", media)
