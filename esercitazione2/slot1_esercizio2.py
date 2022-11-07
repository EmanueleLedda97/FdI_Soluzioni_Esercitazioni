# Scrivere un programma che chieda all’utente di digitare il proprio
# voto preso all’esame d'informatica; se il voto e’ inferiore a 18
# stampare “Esame non passato”.

voto = eval(input("Inserire il proprio voto: "))    # Prendo in input il voto

# Se il voto è inferiore a 18 allora stampo "esame non passato"
if voto < 18:
    print("Esame non passato")  # Stampo il messaggio (dentro l'if)
