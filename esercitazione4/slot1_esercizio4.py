# Salvare in una variabile ‘password’ la stringa “pyth0n”. Il programma dovrà
# chiedere all’utente di indovinare la password, chiedendo in input una
# stringa. Se l’utente indovina la password viene stampato un messaggi con
# scritto “Hai indovinato”, mentre se viene digitata una stringa non corretta
# viene ri-chiesto all’utente di digitare la password. L’utente ha tre
# tentativi per digitare la password, alla fine dei quali, in caso di password
# non indovinata verrà stampato il messaggio “Mi dispiace, hai finito
# i tentativi”.

password_segreta = "pyth0n"     # Creo una variabile che contenga la password segreta
tentativi = 3                   # Creo una variabile per il numero di tentativi

# Finché ho tentativi (quindi numero maggiore di zero) continuo il ciclo
while tentativi > 0:

    # Chiedo all'utente di digitare una password
    password_digitata = input("Digita la password: ")

    # Dopo aver digitato la password decremento i tentativi
    tentativi = tentativi - 1

    # Se la password è stata indovinata esco dal ciclo, altrimenti avviso l'utente che la password è errata
    if password_digitata == password_segreta:
        break
    else:
        print("Password sbagliata. Ti restano", tentativi, "tentativi")

# Avviso l'utente con un messaggio positivo se ha indovinato o negativo se non ha indovinato
if password_digitata == password_segreta:
    print("Congratulazioni! Hai indovinato la password in", 3-tentativi, "tentativi/o")
else:
    print("Mi dispiace, ma hai esaurito i tentativi!")
