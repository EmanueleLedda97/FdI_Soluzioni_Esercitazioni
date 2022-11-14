# Scrivere il programma per la gestione del gioco “black-jack”.
#
# Il gioco prevede che il giocatore parta da un punteggio iniziale di 0, e
# possa pescare quante carte vuole iterativamente. Ogni carta avrà un
# punteggio, e una volta pescata il suo punteggio si sommerà al punteggio
# totale del giocatore.
#
# Il programma deve implementare un meccanismo di iterazione per gestire la
# pesca delle carte: all’inizio di ogni iterazione dovrà essere stampato il
# messaggio “Vuoi pescare una nuova carta? (s/n) ”: se l’utente digita ‘s’
# allora significa che si vuole pescare una carta e quindi verrà effettuata
# un’altra iterazione, mentre se digita ‘n’ allora l’utente non vuole pescare
# altre carte e si fermerà il gioco (quindi il ciclo).
#
# Quando viene scelta l’opzione di pescare una carta il programma deve
# chiedere all’utente di digitare un numero, equivalente al punteggio della
# carta pescata; tale punteggio verrà sommato al punteggio totale del
# giocatore, e se questo supererà il valore 21 allora il gioco s’interromperà
# stampando “hai superato la soglia di 21". Se invece il giocatore si fermerà
# prima di eccedere 21 verrà stampato il punteggio totalizzato.
#
# PRECISAZIONE: Sono possibili tante condizioni d'errore, ed è a discrezione
# vostra come gestirle; non è richiesto niente di particolare, ad esempio, se
# l'utente digita qualcosa di diverso da 's' o 'n' durante il ciclo, o se
# inserisce punteggi negativi.

# Scelta implementativa di questa soluzione: ho scelto di usare 's' come messaggio per pescare,
# e di gestire la condizione mutualmente opposta come condizione d'arresto. Il programma si ferma (non pesco)
# se digito 'n' o se digito qualsiasi altra cosa diversa da 'n'.

# SOLUZIONE: Itero il ciclo fintanto che valgono due condizioni:
# 1) l'utente vuole pescare
# 2) l'utente non ha superato la soglia di 21 punti, come da regolamento
# Se queste condizioni persistono, l'utente può scegliere se pescare una nuova carta o fermarsi.

punteggio = 0
pesca = 's'
while pesca == 's' and punteggio <= 21:

    # Chiedo all'utente se vuole pescare una carta
    pesca = input("Vuoi pescare una carta? (s/n)")

    # Se ha digitato 's' allora aggiungo il punteggio della carta pescata
    if pesca == 's':
        carta = eval(input("Digita il valore della carta pescata: "))
        punteggio = punteggio + carta

# Se il punteggio è inferiore a 21 lo si stampa, altrimenti si avvisa l'utente dicendogli che ha perso
if punteggio <= 21:
    print("Hai totalizzato un punteggio di", punteggio)
else:
    print("Mi dispiace, ma hai sforato il valore 21.")


