# Esercizio 4: Definire una funzione per verificare se un numero sia
# pari o dispari. (N.B. la funzione dovrà restituire un valore booleano)

#   Nome: pari
#
#   Argomenti:
#       - num: numero di cui vogliamo valutare la parità
#
#   Valore di ritorno: Valore di verità circa la parità del numero (True/False)
def pari(num):
    # Se il numero e' pari restituisco il valore booleano True
    if num % 2 == 0:
        return True
    # Altrimenti restituisco il valore False
    else:
        return False
