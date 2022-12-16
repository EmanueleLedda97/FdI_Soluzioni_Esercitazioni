# Esercizio 1: Scrivere un programma che riceva una lista in input
# dall’utente e ne stampi nella shell tutti gli elementi, dal primo
# all’ultimo.

# Prendo in input una lista
lista = eval(input("Digita una lista: "))

# Tramite l'istruzione vado a scorrere elemento per elemento
for el in lista:
    print(el)       # Stampo l'elemento corrente 'el'
