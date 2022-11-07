# Scrivere il programma per la gestione del punteggio di un campionato di calcio.
# Il programma deve chiedere in input tre numeri: numero di partite vinte,
# pareggiate e perse della propria squadra. Il punteggio relativo a ogni esito
# possibile di una partita è il seguente:
#   - vittoria = 3 punti
#   - pareggio = 1 punto
#   - sconfitta = 0 punti
# Calcolare il punteggio ottenuto dalla squadra; se tale punteggio è minore di
# 8 allora il programma dovrà stampare “Squadra retrocessa”, se il punteggio
# è tra 8 e 40 stampare “La tua squadra non ha vinto ma non sara’ retrocessa”,
# e se il punteggio è maggiore di 40 stampare “La tua squadra ha vinto lo scudetto”.

# Assegno a tre variabili i punteggi di ogni possibile esito delle partite
punti_vittoria = 3
punti_pareggio = 1
punti_sconfitta = 0

# Prendo in input il numero di partite vinte, pareggiate e perse
n_vittorie = eval(input("Quante partite ha vinto la tua squadra? "))
n_pareggi = eval(input("Quante partite ha pareggiato la tua squadra? "))
n_sconfitte = eval(input("Quante partite ha perso la tua squadra? "))

# Calcolo il punteggio totale ottenuto
punteggio = n_vittorie * punti_vittoria + n_pareggi * punti_pareggio + n_sconfitte * punti_sconfitta

# Se il punteggio è inferiore a 8 stampo il messaggio contenente la retrocessione
if punteggio < 8:
    print("La tua squadra verra' retrocessa")
else:
    # Se invece la squadra non è retrocessa, se il punteggio è tra 8 e 40 riferisco all'utente
    # che non ha vinto, altrimenti riferisco l'avvenuta vittoria dello scudetto
    if punteggio >= 8 and punteggio <= 40:
        print("La tua squadra non ha vinto ma non verra' retrocessa")
    else:
        print("La tua squadra ha vinto lo scudetto!")

# N.B. e' assolutamente possibile scrivere la condizione così:
#       8 <= punteggio <= 40
# Questa notazione è detta "comparison operator chaining" ed è una formulazione
# che viene spesso consigliata per compattare il codice quando si utilizza il
# linguaggio python; tuttavia, la forma con l'and risulta essere una forma più
# "classica" in informatica, compatibile con larga parte dei linguaggi di programmazione
# e non solo con python, quindi è bene imparare a comprendere a fondo anche la
# condizione con l'and e non solo la versione "compressa".
