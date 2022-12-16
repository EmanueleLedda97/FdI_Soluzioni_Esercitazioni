# Esercizio 3: Chiedere all’utente di digitare una stringa e verificare se il
# primo elemento della stringa è uguale all’ultimo elemento (suggerimento:
# per indicizzare l’ultimo elemento si usa l’indice -1)

mia_stringa = input("Digita una stringa: ")

# Confronto il primo elemento indicizzandolo tramite l'indice zero, con l'ultimo elemento
# indicizzandolo con indice -1
if mia_stringa[0] == mia_stringa[-1]:
    print("La stringa ha il primo elemento uguale all'ultimo")
else:
    print("La stringa non ha il primo elemento uguale all'ultimo")
