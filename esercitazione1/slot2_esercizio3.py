# Stampare la media aritmetica di due numeri acquisiti tramite la funzione
# input (si ricordi di usare la funzione eval).

# Usiamo la funzione input per prendere la STRINGA in input equivalente
# ad un numero, e utilizziamo la funzione eval per valutare il valore
# del numero contenuto nella stringa.
num1 = eval(input("Digita il primo numero: "))      # Prendo in input il primo numero e lo valuto (eval)
num2 = eval(input("Digita il secondo numero: "))    # Prendo in input il secondo numero e lo valuto (eval)

media = (num1 + num2) / 2   # Calcolo la media aritmetica tra i due numeri presi in input
print(media)                # Operazione Opzionale: stampo il valore della media
