# Scrivere un programma che acquisisca attraverso la tastiera la lunghezza
# del lato di un quadrato e ne stampi nella shell l’area (lato per lato)
# e il perimetro (lato per quattro).

lato = eval(input("Digita il valore del lato: "))   # Prendo in input il lato e lo valuto
area = lato * lato      # Calcolo l'area del quadrato
perimetro = lato * 4    # Calcolo il perimetro del quadrato

# Stampo il messaggio concatenando stringhe e variabili opportune
print("Il quadrato di lato", lato, "ha come area", area, "e come perimetro", perimetro)