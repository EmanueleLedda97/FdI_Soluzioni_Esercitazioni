# Esercizio 4: Scrivere un programma che prenda in ingresso
# 5 numeri e ne calcoli la media dei valori assoluti.

# Creo una variabile per salvare la somma cumulativa
somma = 0

# Itero il ciclo 5 volte
n = 5
k = 0
while k < n:
    numero_corrente = eval(input("Digita un numero: "))     # Prendo in input un numero
    somma = somma + abs(numero_corrente)                    # Sommo cumulativamente il valore assoluto
    k = k + 1

media_dei_valori_assoluti = somma / n       # Calcolo la media dei valori assoluti
print(media_dei_valori_assoluti)            # Stampo la media
