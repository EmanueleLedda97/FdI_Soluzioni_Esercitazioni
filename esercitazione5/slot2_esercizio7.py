# Esercizio 7: Definire la funzione ‘norma_2D’ che prende in ingresso
# due numeri (‘x’, ‘y’) che corrispondono alle coordinate x e y di un
# punto nel piano, e un numero ‘p’. La funzione deve calcolare la norma
# p del vettore [x, y].

#   Nome: norma_2d
#
#   Argomenti:
#       - x: coordinata x del punto di cui vogliamo calcolare la norma p
#       - y: coordinata y del punto di cui vogliamo calcolare la norma p
#       - p: norma selezionata
#
#   Valore di ritorno: norma p del punto [x, y]
def norma_2d(x, y, p):
    norma_p = (abs(x) ** p + abs(y) ** p) ** (1 / p)
    return norma_p
