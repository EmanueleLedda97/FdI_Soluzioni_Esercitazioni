# Esercizio 2: Scrivere un programma che chieda all'utente di inserire una
# sequenza di numeri (dopo averne chiesto la lunghezza), li memorizzi in una
# lista e stampi quest'ultima nella shell.

# Prendo in input la lunghezza della lista
lunghezza_lista = eval(input("Quanti numeri vuoi digitare? "))

la_mia_lista = []               # Creo una lista inizialmente vuota
k = 0                           # Inizializzo a zero il contatore
while k < lunghezza_lista:
    numero_corrente = eval(input("Digita un numero: "))     # Chiedo in input un numero...
    la_mia_lista = la_mia_lista + [numero_corrente]         # ... e lo aggiungo alla lista

# Infine stampo la lista appena creata
print(la_mia_lista)

# N.B.; qui se dobbiamo aggiungere cumulativamente elementi alla lista dobbiamo ricordarci
# che possiamo farlo tramite l'operatore di concatenazione '+'. TUTTAVIA, tale operatore
# funziona solo tra stringhe, quindi non posso fare ad esempio [1,2,3] + 4, e se voglio aggiungere
# l'elemento 4 alla lista dovrò creare una lista (detta in matematica 'insieme singoletto', o 'singleton'
# in inglese), contenete l'elemento 4. In sostanza, ricordarci di mettere le quadre intorno all'elemento
# da concatenare!
#
# CORRETTO
# [1, 2, 3] + [4]
#
# SBAGLIATO
# [1, 2, 3] + 4
