# Usare la funzione input per acquisire il nome e il cognome dell'utente,
# e memorizzare tali valori in due variabili distinte. Assegnare a una nuova
# variabile una stringa che contenga il nome e il cognome dell'utente
# (ottenuta mediante concatenazione), separati da uno spazio.
# Stampare poi nella shell il valore di tale variabile.

# Per acquisire i nomi usiamo la funzione input. Ricordiamo che la funzione input
# prende come parametro una stringa che verrà stampata come messaggio di output
# prima di acquisire l'input da parte dell'utente. Ricordiamoci poi di salvare
# il risultato dell'input dentro ad una variabile opportuna, che conterrà la STRINGA
# equivalente all'input digitato dall'utente (se volessimo trasformare la stringa in
# numero occorrerà usare eval, che in questo caso non serve in quanto nome e cognome
# rappresentano delle stringhe)
nome = input("Digita il tuo nome: ")            # Chiedo in input il nome
cognome = input("Digita il tuo cognome: ")      # Chiedo in input il cognome
nominativo = nome + " " + cognome               # Concateno nome e cognome separati da uno spazio
print(nominativo)                               # Stampo il nominativo
