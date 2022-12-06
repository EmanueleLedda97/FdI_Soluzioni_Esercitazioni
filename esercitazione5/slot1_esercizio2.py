# Esercizio 2: Scrivere un programma che acquisisca due stringhe,
# e determini quale sia la più lunga usando la funzione len.

stringa1 = input("Digita la prima stringa: ")       # Prendo in input la prima stringa
stringa2 = input("Digita la seconda stringa: ")     # Prendo in input la seconda stringa

# Con la funzione 'len' calcolo la lunghezza delle stringhe per poterle confrontare
if len(stringa1) > len(stringa2):
    print("La prima stringa e' piu' lunga della seconda")
elif len(stringa1) < len(stringa2):
    print("La seconda stringa e' piu' lunga dalla seconda")
else:
    print("Le due stringhe hanno la stessa lunghezza")
