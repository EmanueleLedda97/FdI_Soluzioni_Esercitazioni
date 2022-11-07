# Assegnare a due variabili di nome 'moltiplicando' e 'moltiplicatore' i valori
# 10 e 30, assegnare il loro prodotto a una variabile di nome 'prodotto' e
# stampare nella shell il seguente messaggio, facendo in modo che al posto
# dei puntini di sospensione compaiano i valori delle variabili corrispondenti:
# “Il prodotto tra ... e ... è …”

moltiplicando = 10      # Assegno a 'moltiplicando' il valore 10
moltiplicatore = 30     # Assegno a 'moltiplicatore' il valore 30
prodotto = moltiplicatore * moltiplicando   # assegno a 'prodotto' il prodotto tra le due variabili

# Uso la print per stampare il messaggio. Notare che questa volta non passiamo un solo
# parametro alla funzione print, bensì 6 parametri tutti separati da virgole; questi
# parametri possono essere stringhe, numeri, variabili etc., ed quello che farà la funzione
# sarà concatenare tutti i valori passati inserendo uno spazio tra un valore e l'altro.
print("Il prodotto tra", moltiplicando, "e", moltiplicatore, "e'", prodotto)

