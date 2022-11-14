# Chiedere all’utente di digitare la lista dei voti che ha preso nei vari
# corsi: il programma dovrà avvisare l’utente con il messaggio “Hai altri
# corsi da inserire? (s/n)”; se l’utente digita ‘s’ allora il programma
# prenderà in input due numeri, uno relativo al voto dell’esame e l’altro
# al numero di cfu, se invece l’utente digita ‘n’ allora il ciclo si arresterà.
# Alla fine dell’esecuzione il programma deve stampare la media
# ponderata dei voti (fare riferimento alle slides se non ci si ricorda come
# calcolare la media ponderata).

# Soluzione: similmente alla media aritmetica, mi devo salvare la somma cumulativa, ma questa
# volta andrà pesata con i cfu relativi:
#       somma_pesata = somma_pesata + voto * cfu
# insieme alla somma pesata devo anche salvarmi la somma dei cfu per dividere al denominatore
#       totale_cfu = totale_cfu + cfu

# Dichiaro due variabili per salvare la somma pesata ed il totale di cfu degli esami
somma_pesata = 0
totale_cfu = 0

# Creo una variabile per tener traccia della scelta dell'utente, che simboleggerà:
# 's' -> Sì, l'utente vuole digitare altri corsi nella lista
# 'n' -> No, l'utente non vuole digitare altri corsi nella lista
# altro -> Stato non definito
scelta = 's'
while scelta == 's':

    # Mando la scelta in stato non definito, in quanto non so se al prossimo giro
    # l'utente vorrà digitare un altro corso. La variabile 'scelta' verrà aggioranta
    # alla fine di questo ciclo, chiedendo all'utente se vuole inserire altri corsi
    scelta = 'ND'

    # Prendo in input il voto e i cfu dell'esame digitato
    voto = eval(input("Digita il voto preso all'esame: "))
    cfu = eval(input("Digita il numero di cfu dell'esame: "))

    # Calcolo la somma pesata ed il totale dei cfu
    somma_pesata = somma_pesata + voto * cfu
    totale_cfu = totale_cfu + cfu

    # Chiedo all'utente di inserire 's' o 'n', e finché non digita una di queste due lettere il
    # programma non andrà avanti
    while scelta != 's' and scelta != 'n':
        # Chiedo all'utente se vuole digitare altri corsi
        scelta = input("Hai altri corsi da inserire (s/n)? ")

        if scelta != 's' and scelta != 'n':
            print("Attenzione, devi digitare 's' per sì, o 'n' per no, non puoi digitare", scelta)

# Calcolo la media ponderata e la stampo
media = somma_pesata / totale_cfu
print("La media dei tuoi voti e'", media)
