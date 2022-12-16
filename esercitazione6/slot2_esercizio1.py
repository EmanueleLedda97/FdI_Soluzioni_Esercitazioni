# Esercizio 1: Chiedere all’utente di inserire il suo nome e cognome separati
# da uno spazio; successivamente, salvare in una lista le due stringhe relative
# una al nome ed una al cognome (suggerimento: occorre usare split)

# Prendo in input il nome e cognome separati da uno spazio
nominativo = input("Digita il tuo nome e cognome: ")

# Separo nome e cognome con la funzione split, li salvo in una lista, e assegno i valori a due variabili distinte
lista_nome_e_cognome = nominativo.split()
nome = lista_nome_e_cognome[0]              # Assegno il nome
cognome = lista_nome_e_cognome[1]           # Assegno il cognome
