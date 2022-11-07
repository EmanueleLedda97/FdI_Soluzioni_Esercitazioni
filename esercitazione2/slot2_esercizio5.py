# Chiedere all’utente di digitare due numeri “dividendo” e “divisore”,
# e stampare “Divisibile” se il dividendo è divisibile per il divisore
# (ovvero se il resto della loro divisione intera equivale a zero)

dividendo = eval(input("Digitare il dividendo: "))      # Prendo in input il dividendo
divisore = eval(input("Digitare il divisore: "))        # Prendo in input il divisore

# Se il resto della divisione (ottenuto usando l'operatore modulo '%') tra dividendo e
# divisore è uguale a zero allora significa che il dividendo è divisibile per il divisore
if dividendo % divisore == 0:
    print(dividendo, "e' divisibile per", divisore)         # Stampo il messaggio nell'if
else:
    print(dividendo, "non e' divisibile per", divisore)     # Stampo il messaggio nell'else
