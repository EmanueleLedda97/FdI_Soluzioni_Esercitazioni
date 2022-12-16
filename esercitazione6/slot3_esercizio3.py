# Esercizio 3: Scrivere un programma che riceva una lista di numeri interi
# dall’utente e creare una lista contenente solo i numeri pari digitati
# dall’utente. Infine stampare la lista

# Prendo in input una lista dall'utente
lista_digitata = eval(input("Digita una lista di numeri interi: "))

# Creo una lista (inizialmente vuota) dove inserire i numeri pari della lista originale
lista_pari = []
for el in lista_digitata:
    if el % 2 == 0:
        lista_pari = lista_pari + [el]

# Stampo infine la lista dei numeri pari
print(lista_pari)
