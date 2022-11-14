# Scrivere un programma che chieda all’utente di digitare il numero 42:
# il programma deve poi acquisire l’input da parte dell’utente, e se
# non si tratta del numero 42 deve mandare il messaggio “Numero errato”,
# e dovrà richiedere nuovamente all’utente di digitare il numero 42.
# Il programma terminerà quando l’utente digiterà il numero 42, e il
# programma stamperà “Numero corretto”.


password_segreta = 42       # Creo una variabile per contenere la 'password' che è il numero 42
password_digitata = 0       # Creo poi una varibaile per contenere la 'password' che l'utente digiterà

# Finché la password digitata è diversa da quella segreta allora viene ripetuto i ciclo
while password_digitata != password_segreta:
    password_digitata = eval(input("Digita il numero segreto:  "))  # Prendo l'input dall'utente

    # Controllo se l'input digitato corrisponde alla password: se ciò non avviene stampo un messaggio d'avviso
    if password_digitata != password_segreta:
        print("Il numero e' errato! Riprova")

# Una volta terminato il ciclo, e quindi una volta digitata la password corretta, stampo il messaggio
print("Numero corretto!")
