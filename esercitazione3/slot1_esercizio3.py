# Chiedere all’utente di digitare un numero intero 'n', e stampare tutti i
# numeri pari tra 0 ed n (decidete voi se comprendere o meno 'n').

n = eval(input("Digita un numero: "))   # Chiedo l'input all'utente

k = 0       # Inizializzo il contatore a zero

# Ripeto il ciclo finché k risulta minore di n
while k <= n:
    print(n)    # Stampo il numero n
    n = n + 2   # Incremento A DUE A DUE il valore k. Così facendo preservo la parità del contatore

# N.B. questa soluzione agisce sul fattore di incremento, agendo incrementando 'di due' anziché 'di uno'
# ad ogni iterazione. Questo ha come effetto il preservare la parità del contatore, poiché se, partendo da 0,
# continuo ad aggiungere 2, il numero rimarrà pari, e otterrò a ogni iterazione il numero pari successivo.
# Fra i vari modi per svolgere l'esercizio, esiste un modo altrettanto corretto, che però risulta essere
# più "computazionalmente oneroso", nel senso che è una soluzione che richiede all'interprete di eseguire
# più istruzioni.
#
# k = 0
# while k <= n:
#     if k % 2 == 0:
#         print(k)
#     k = k + 1
#
# Questa soluzione ha come idea quella di iterare tutti i numeri da 0 a n, quindi 1,2,3,...,n
# ma stampiamo SOLO quando il contatore assume un valore pari. In questo modo il ciclo esegue
# 'n' iterazioni, mentre la prima soluzione proposta, se ci si riflette un attimo, non esegue
# 'n' iterazioni, ma ne esegue la metà, 'n/2' iterazioni, in quanto sto incrementando a due a due.
