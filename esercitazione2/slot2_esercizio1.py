# Chiedere all’utente di digitare due numeri. Se il primo numero
# risulta maggiore del secondo stampare la stringa “Il maggiore e’
# il primo”, altrimenti stampare la stringa “Il maggiore e’ il secondo”
# N.B.: Non vi e' richiesto di gestire il caso in cui siano uguali i numeri
# quindi gestitelo come preferite.

num1 = eval(input("Digita il primo numero: "))      # Prendo in input il primo numero
num2 = eval(input("Digita il secondo numero: "))    # Prendo in input il secondo numero

# Se num1 è maggiore di num2 entro nel ramo dell'if, e stampo un messaggio dove viene
# detto che il primo è maggiore; altrimenti entro nel ramo dell'else, e viene stampato
# un messaggio che avviserà l'utente che il maggiore è il secondo.
if num1 > num2:
    print("Il primo numero è maggiore")     # Stampo il messaggio (dentro l'if)
else:
    print("Il secondo numero è maggiore (o al limite uguale al primo)")     # Stampo il messaggio (dentro l'else)

# N.B. Volendo, è anche possibile invertire la condizione num2 < num1, oppure invertire i due rami:
# ad esempio potevamo scrivere if num1 < num2, e stampare "il secondo è maggiore",
# e nel ramo dell'else catturare il caso opposto.
# In generale, usiamo l'if-else quando abbiamo condizioni dette "mutualmente esclusive", ovvero
# quando una esclude l'altra, ed è a nostra discrezione come organizzare i rami if ed else, l'importante
# è che rimangano consistenti secondo la semantica del programma che vogliamo scrivere.

