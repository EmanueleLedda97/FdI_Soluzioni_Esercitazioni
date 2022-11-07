# Scrivere un programma che chieda all’utente d'inserire la propria età:
# se il numero digitato è negativo stampare “L’eta’ digitata non e’
# corretta”, altrimenti stampare “Sei maggiorenne” o “Sei minorenne”
# in base all’età della persona.

eta = eval(input("Digita la tua eta: "))    # Prendo in input l'eta

# Se l'eta' è minore di zero significa che è negativa e che non può essere un'età valida
if eta < 0:
    print("L'eta' digitata non e' corretta! Non può assumere valori negativi")  # Messaggio dentro al primo if
else:
    # Se l'età è valida (quindi siamo dentro al ramo else) controllo se sia maggiore
    # o uguale a 18; se lo è stampo "sei maggiorenne" altrimenti "sei minorenne
    if eta >= 18:
        print("Sei maggiorenne")    # Stampo il messaggio nell'if "annidato" (quindi il più interno)
    else:
        print("Sei minorenne")      # Stampo il messaggio nell'else "annidato"

# N.B. quando un if o un if-else è a sua volta dentro un altro ramo if o if-else allora si dice
# che quell'if o if-else è "annidato" dentro al primo if o if-else. Non ci sono limiti alla
# "profondità" degli annidamenti: possiamo annidare tante istruzioni condizionali l'una dentro all'altra
