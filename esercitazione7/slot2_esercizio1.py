# Esercizio 1.1: Creare il dizionario ‘passaporto’, contenente come chiavi
# ‘nome’, ‘cognome’, ‘nazionalita’, ‘anno_nascita’, ‘altezza’ e ‘colore_capelli’.
# Determinare i valori della variabile passaporto chiedendo all’utente di inserire i propri dati,
# tramite la definizione della funzione ‘compila_passaporto’ (o ‘popola_passaporto’).
#
# Esercizio 1.2: Creare la funzione ‘determina_maggiore_eta’ che prende in
# ingresso un dizionario contenente un passaporto, e determinare se il passaporto
# si riferisce ad una persona maggiorenne.
#
# Esercizio 1.3: Creare la funzione ‘parentela’ che prende in ingresso due passaporti
# e determini se si tratta di due elementi dello stesso nucleo familiare (si usi la
# corrispondenza dei cognomi come metrica per verificare la parentela).
#
# Esercizio 1.4: Creare un passaporto tramite la funzione ‘compila_passaporto’ definita
# ad esercizio 1.1; dopodiché aggiornare il valore dell’altezza, inserendo un nuovo
# valore (per modificarne il valore occorre indicizzare la chiave ‘altezza’ ed
# assegnarvi il nuovo valore).


# 1.1
def popola_passaporto():
    passaporto = {}
    passaporto['nome'] = input("Digita il tuo nome: ")
    passaporto['cognome'] = input("Digita il tuo cognome: ")
    passaporto['nazionalita'] = input("Digita la tua nazionalita': ")
    passaporto['anno_nascita'] = eval(input("Digita il tuo anno di nascita: "))
    passaporto['altezza'] = eval(input("Digita la tua altezza: "))
    passaporto['colore_capelli'] = input("Digita il colore dei tuoi capelli: ")
    return passaporto


# 1.2
def determina_maggiore_eta(passaporto):
    esito = False
    anno_corrente = 2022
    eta = anno_corrente - passaporto['anno_nascita']
    if eta > 18:
        esito = True
    return esito


# 1.3
def parentela(pass1, pass2):
    return pass1['cognome'] == pass2['cognome']


# 1.4
mio_passaporto = popola_passaporto()
mio_passaporto['altezza'] = 1.75