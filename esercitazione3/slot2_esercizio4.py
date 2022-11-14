# Chiedere all’utente di digitare un numero intero tra 1 e 7; se l’utente
# non digita un numero nell’intervallo mandare un messaggio di errore e
# chiedere all’utente di ri-digitare un numero. Dopodiché stampare il giorno
# della settimana relativo al numero selezionato. esempio: se l’utente digita 3:
#   "Il giorno numero 3 e' il Mercoledi"

# Creo una variabile per contenere l'indice del giorno, a cui all'inizio do' zero
# per consentire l'entrata dentro al while
giorno = 0

# finché il giorno non è tra 1 e 7 ripeto la richiesta di inserire un giorno valido
while giorno < 1 or giorno > 7:
    n = eval(input("Digita un numero tra 1 e 7: "))   # Chiedo l'input all'utente

    # Se l'input non è adeguato (non è tra 1 e 7) avviso l'utente
    if giorno < 1 or giorno > 7:
        print("Attenzione,", giorno, "non e' compreso fra 1 e 7")

if giorno == 1:
    print("Il giorno numero", giorno, "e' il Lunedi")
if giorno == 2:
    print("Il giorno numero", giorno, "e' il Martedi")
if giorno == 3:
    print("Il giorno numero", giorno, "e' il Mercoledi")
if giorno == 4:
    print("Il giorno numero", giorno, "e' il Giovedi")
if giorno == 5:
    print("Il giorno numero", giorno, "e' il Venerdi")
if giorno == 6:
    print("Il giorno numero", giorno, "e' il Sabato")
if giorno == 7:
    print("Il giorno numero", giorno, "e' la Domenica")

# N.B. nelle condizioni a cascata simili a questa si può anche usare la condizione contratta dell' else-if,
# ovvero la condizione 'elif'. Di solito questa risulta più utile quando si hanno una serie di N condizioni
# da "catturare" (come nel nostro caso, sette condizioni) e poi alla fine una condizione per catturare tutti
# i valori che non ricadono nelle N condizioni. Quindi in questo esempio anche dei semplici if vanno bene
# perché non è condizione di "default", mi sono assicurato prima che il numero fosse tra 1 e 7.
#
# esempio elif:
#
# if condizione1:
#     print("Siamo nel caso 1")
# elif condizione2:
#     print("Siamo nel caso 2")
# elif condizione3:
#     print("Siamo nel caso 3")
# elif condizione4:
#     print("Siamo nel caso 4")
# else:
#     print("Non siamo in nessuna delle condizioni precedenti")

