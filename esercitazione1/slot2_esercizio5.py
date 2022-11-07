# Scrivere un programma che chieda all’utente un numero intero e stampi il
# numero precedente e quello successivo.

numero = eval(input("Digita un numero: "))      # Prendo in input un numero e lo valuto
successivo = numero + 1     # Calcolo il successivo
precedente = numero - 1     # Calcolo il precedente
print(numero, "ha come successivo", successivo, "e come precedente", precedente)    # Stampo il messaggio
