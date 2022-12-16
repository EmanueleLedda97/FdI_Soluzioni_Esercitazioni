# Esercizio 2.1: Creare un dizionario ‘data’ contenente tre chiavi: ‘anno’,
# ‘mese’ e ‘giorno’, in formato numerico.  Determinare i valori del dizionario
# chiedendo all’utente di inserire i propri dati, tramite la definizione della
# funzione ‘compila_data’ (o ‘popola_data’).
#
# Esercizio 2.2: Creare la funzione ‘verifica_integrita_data’ che prende in ingresso
# un dizionario di tipo ‘data’, e ne verifichi l’integrità: per verificare
# l’integrità si intende controllare che il mese sia compreso tra 1 e 12, che
# il giorno sia compreso tra 1 e 31 e che l’anno sia non negativo.
# La funzione deve restituire True se ne viene verificata l’integrità, False altrimenti.
#
# Esercizio 2.3: Creare la funzione ‘scaduto’ che verifichi se una certa data
# è già rispetto ad oggi 14/12/2022.
#
# Esercizio 2.4: Creare la funzione ‘compara_date’ che prende in ingresso due date
# e restituisca 1 se la prima data è antecedente alla secondo o 2 viceversa.
#
# Esercizio 2.5: Usando come base il dizionario ‘passaporto’ definito nell’esercizio
# 1, aggiungere al campo del passaporto il campo ‘data_di_emissione’ e ‘data_di_scadenza’,
# formattati come due dizionari di tipo ‘data’.


# 2.1
def popola_data():
    data = {}
    data['giorno'] = eval(input("Digita il giorno in formato numerico"))
    data['mese'] = eval(input("Digita il mese in formato numerico"))
    data['anno'] = eval(input("Digita l'anno in formato numerico"))
    return data


# 2.2
def verifica_integrita_data(data):
    data_integra = True

    # Controllo integrità giorno
    if data['giorno'] < 1 or data['giorno'] > 31:
        data_integra = False

    # Controllo integrità mese
    if data['mese'] < 1 or data['mese'] > 12:
        data_integra = False

    # Controllo integrità anno
    if data['anno'] < 1:
        data_integra = False

    return data_integra


# 2.3
def scaduto(data):
    data_scaduta = False

    giorno_corrente = 14
    mese_corrente = 12
    anno_corrente = 2022

    # Se l'anno è uguale...
    if data['anno'] == anno_corrente:
        # ... e anche il mese è uguale...
        if data['mese'] == mese_corrente:
            # ... allora controllo il giorno. Se è antecedente al giorno corrente è la data scaduta
            if ['giorno'] > giorno_corrente:
                data_scaduta = True
        # ... e il mese non è uguale ...
        else:
            # ... allora controllo se il mese è antecedente al giorno corrente: se lo è, allora è la data scaduta
            if data['mese'] > mese_corrente:
                data_scaduta = True
    # Se l'anno è diverso ...
    else:
        # ... allora controllo se è antecedente all'anno corrente: in caso affermativo, allora è la data scaduta
        if data['anno'] > anno_corrente:
            data_scaduta = True

    # Restituisco l'esito
    return data_scaduta


#2.4
il_mio_passaporto = {
    'nome': 'Mario',
    'cognome': 'Rossi',
    'nazionalita': 'Italiana',
    'altezza': 1.76,
    'colore_capelli': 'castani'
}

il_mio_passaporto['data_di_emisione'] = popola_data()
il_mio_passaporto['data_di_scadenza'] = popola_data()

if scaduto(il_mio_passaporto['data_di_scadenza']):
    print("Il tuo passaporto e' scaduto il", il_mio_passaporto['data_di_scadenza'])
else:
    print("Il tuo passaporto scadra' il", il_mio_passaporto['data_di_scadenza'])
