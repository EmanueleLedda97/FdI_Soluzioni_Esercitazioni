# Chiedere all’utente di digitare il proprio anno di nascita.
# Il programma deve, prima di tutto, verificare che il numero digitato
# sia positivo (altrimenti avvisare con un messaggio di errore), e
# deve successivamente stampare la generazione di appartenenza dell’utente,
# tenendo conto della seguente suddivisione:
#       1965-1980: Generazione X
#       1981-1996: Generazione Y
#       1997-2012: Generazione Z
# Se l’utente digita un numero minore di 1964 o maggiore di 2012 il
# programma dovrà stampare il messaggio “Non abbiamo dati sulla tua generazione”.

anno_nascita = eval(input("Digita il tuo anno di nascita: "))   # Prendo in input l'anno di nascita

# Se l'anno digitato è negativo avviso l'utente con un messaggio di errore.
if anno_nascita < 0:
    print("Attenzione! L'anno digitato non e' valido, inserire un numero non negativo")
else:
    # Se (if) l'anno digitato è fuori range, avvisiamo che non abbiamo dati.
    # Altrimenti (else) catturiamo l'intervallo equivalente alla generazione da stampare in output
    if anno_nascita < 1965 or anno_nascita > 2012:
        print("Non abbiamo dati per la tua generazione")
    else:
        if anno_nascita >= 1965 and anno_nascita <= 1980:
            print("Se sei nato nel", anno_nascita, "fai parte della Generazione X")
        if anno_nascita >= 1981 and anno_nascita <= 1996:
            print("Se sei nato nel", anno_nascita, "fai parte della Generazione Y")
        if anno_nascita >= 1997 and anno_nascita <= 2012:
            print("Se sei nato nel", anno_nascita, "fai parte della Generazione Z")

# Di seguito una versione alternativa che utilizza il 'comparison operator chaining':
# if anno_nascita < 0:
#     print("Attenzione! L'anno digitato non e' valido, inserire un numero non negativo")
# else:
#     if 1965 <= anno_nascita <= 1980:
#         print("Se sei nato nel", anno_nascita, "fai parte della Generazione X")
#     if 1981 <= anno_nascita <= 1996:
#         print("Se sei nato nel", anno_nascita, "fai parte della Generazione Y")
#     if 1997 <= anno_nascita <= 2012:
#         print("Se sei nato nel", anno_nascita, "fai parte della Generazione Z")
