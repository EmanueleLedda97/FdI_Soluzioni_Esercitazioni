# Esercizio 3: Definire una funzione per calcolare il valore assoluto
# di un numero (senza usare la libreria math).

#   Nome: valore_assoluto
#
#   Argomenti:
#       - num: il numero di cui si vuol calcolare il valore assoluto
#
#   Valore di ritorno: il valore assoluto del numero
def valore_assoluto(num):
    if num > 0:
        return num
    else:
        return -num
