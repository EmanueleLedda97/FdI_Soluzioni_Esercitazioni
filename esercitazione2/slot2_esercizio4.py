# Scrivere un programma che chieda all’utente di digitare il
# proprio voto preso all’esame d'informatica; se il voto e’
# inferiore a 0 o maggiore di 30 stampare “Il voto digitato
# non e’ valido”, altrimenti stampare “Esame passato” o “Esame
# non passato” a seconda del voto (>18 esame passato).

voto = eval(input("Digita il tuo voto: "))  # Prendo in input il voto

# Se il voto è inferiore a 0 o maggiore di 30 avviso l'utente con un messaggio.
# Ho usato OR perché mi interessa che una delle due consizioni valga: o il numero è negativo,
# e non va bene, o il numero è maggiore di 30, e non va bene ugualmente. Entrambe le condizioni
# innescano l'entrata dentro al ramo if, nel quale è contenuto il messaggio di errore
if voto < 0 or voto > 30:
    print("Il voto digitato non e' valido!")    # Stampo il messaggio nell'if esterno
else:
    # Una volta che so che il voto è valido (sono dentro l'else), allora controllo
    # se il voto è maggiore o uguale a 18 e stampo "esame passato" altrimenti "esame non passato"
    if voto >= 18:
        print("Esame passato")          # Stampo il messaggio nell'if annidato
    else:
        print("Esame non passato")      # Stampo il messaggio nell'esle annidato

# N.B. questo non era l'unico modo, di seguito metto altre due possibilità.
# Occhio che nelle seguenti possibilità ho messo la condizione mutualmente opposta nell'if
# e quindi ho scambiato i contenuti del ramo if ed else.

# ALTERNATIVA 1 (And Operator)
# if voto >= 0 and voto <= 30:
#     if voto >= 18:
#         print("Esame passato")
#     else:
#         print("Esame non passato")
# else:
#     print("Il voto digitato non e' valido!")

# ALTERNATIVA 2 (Comparison Operator Chaining)
# if 0 <= voto <= 30:
#     if voto >= 18:
#         print("Esame passato")
#     else:
#         print("Esame non passato")
# else:
#     print("Il voto digitato non e' valido!")
