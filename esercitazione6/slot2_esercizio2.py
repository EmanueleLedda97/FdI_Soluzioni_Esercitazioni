# Esercizio 2: Scrivere la funzione ‘verifica_animale’ che prende in ingresso il
# nome di un animale restituisca True/False verificando se l’animale inizia con
# la lettera “E”. Successivamente, chiedere all’utente di digitare il nome di
# un’animale, e verificare se l’animale inizia con la lettera “E” usando la funzione
# appena definita.

# Creo la funzione per verificare la lettera iniziale dell'animale
def verifica_animale(nome_animale):

    # Creo una variabile dove salvare l'esito (positivo o negativo) della condizione
    esito = False

    # Se la stringa 'nome_animale' ha come primo carattere la 'E' o la 'e' allora l'esito va a True
    if nome_animale[0] == 'E' or nome_animale[0] == 'e':
        esito = True

    # Infine restituisco l'esito
    return esito


# Chiedo in input il nome di un animale
il_mio_animale = input("Digita un animale: ")

# Controllo tramite la funzione appena definita se l'animale inizia con la lettera 'E'
if verifica_animale(il_mio_animale):
    print("L'animale inizia per 'E'")
else:
    print("L'animale non inizia per 'E'")
