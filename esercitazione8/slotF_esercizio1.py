# Esercizio 1.1: Aprire il file ‘lettera_di_natale1.txt’ contenuto nella cartella ‘Root/slot_F’ in modalità
# lettura. Creare un dizionario ‘lettera’ contenente tre campi: il nome, l’età e il dono richiesto da parte
# del bambino. Compilare i campi del dizionario leggendo questi tre valori dalle tre righe del file.
f = open('Root/slot_F/lettera_di_natale_1.txt', 'r')
valori = f.readlines()
f.close()

lettera1 = {
    'nome': valori[0][:-1],         # Qui il '[:-1]' indica uno slicing per eliminare l'andata a capo
    'eta': eval(valori[1][:-1]),    # Qui ricordiamo eval poiché vogliamo memorizzare un numero
    'dono': valori[2]               # QUi non occorre fare slicing in quanto l'ultima riga non ha l'andata a capo
}


# Esercizio 1.2: Fare la stessa cosa con il file ‘lettera_di_natale2.txt’, e determinare quale
# dei due bambini ha l’età maggiore.
f = open('Root/slot_F/lettera_di_natale_2.txt', 'r')
valori = f.readlines()
f.close()

lettera2 = {
    'nome': valori[0][:-1],         # Qui il '[:-1]' indica uno slicing per eliminare l'andata a capo
    'eta': eval(valori[1][:-1]),    # Qui ricordiamo eval poiché vogliamo memorizzare un numero
    'dono': valori[2]               # QUi non occorre fare slicing in quanto l'ultima riga non ha l'andata a capo
}

if lettera1['eta'] != lettera2['eta']:
    if lettera1['eta'] > lettera2['eta']:
        print("Il bambino piu' grande e' quello che ha scritto la prima lettera")
    else:
        print("Il bambino piu' grande e' quello che ha scritto la seconda lettera")
else:
    print("I due bambini hanno l'età uguale")

# Esercizio 1.3: Aprire in modalità lettura il file ‘lettera_aperta_a_babbo_natale.txt’, e leggerne
# il contenuto. Determinare quante parole ha scritto il bambino: se è stato ‘bravo’ e ha scritto almeno
# trenta parole nella lettera allora stampare il messaggio ‘riceverai dei doni quest’anno’, altrimenti stampare
# il messaggio ‘non riceverai alcun dono quest’anno’.
f = open('Root/slot_F/lettera_aperta_a_babbo_natale.txt', 'r')
testo_lettera = f.read()
f.close()

numero_parole = len(testo_lettera.split())
if numero_parole >= 30:
    print("Hai scritto", numero_parole, "parole: riceverai dei doni quest'anno!")
else:
    print("Hai scritto", numero_parole, "parole: non riceverai doni quest'anno!")

# Esercizio 1.4: Leggere il contenuto del file ‘menu_cenone_di_natale.txt’: per ogni pietanza stampare
# ‘la pietanza X è buona” o “la pietanza X non è buona”, seguendo il criterio di affermare che una pietanza
# è buona quando inizia per lettera ‘P’ o ‘A’, tenendo conto che, tuttavia, il ‘Pandoro’ non è
# considerato una buono.
f = open('Root/slot_F/menu_cenone_di_natale.txt', 'r')
menu = f.readlines()
f.close()

for pietanza in menu:
    # Se la pietanza corrente è una stringa che contiene l'andata a capo la rimuovo con uno sliging
    if '\n' in pietanza:
        pietanza = pietanza[:-1]

    # Controllo se la prima lettera è 'P', 'p', 'A', o 'a', con l'operatore 'in', e verifico anche che non sia Pandoro
    if pietanza[0] in 'PpAa' and pietanza != 'Pandoro':
        print("La pietanza '", pietanza, "' e' considerata buona")
    else:
        print("La pietanza '", pietanza, "' non e' considerata buona")