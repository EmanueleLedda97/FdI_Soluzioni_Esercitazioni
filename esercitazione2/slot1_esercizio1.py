# Scrivere un programma che chieda all’utente d'inserire la propria età,
# e stampare a video “Sei maggiorenne” se l’età inserita è maggiore o uguale a 18.

eta = eval(input("Inserisci la tua eta': "))    # Prendo in input l'età

# Utilizzo l'istruzione condizionale if, imponendo come condizione
# "se eta maggiore o uguale a 18", allora stampo il messaggio
if eta >= 18:
    print("Sei maggiorenne")    # Stampo il messaggio (dentro l'if)
