# Chiedere all’utente di digitare un numero intero e determinare se si tratta
# di un quadrato perfetto (N.B. con quadrato perfetto si intende un numero
# intero che può essere scritto nella forma x*x, dove x è un numero intero)

# N.B. in python esiste un modo semplice mediante operatori aritmetici per risolvere
# questo esercizio, ma qui verrà fornita una soluzione iterativa che tiene conto delle
# proprietà dei numeri interi.
# La soluzione è da intendere come un semplice esercizio per familiarizzare con l'istruzione
# iterativa e con il ragionamento tramite cicli, e non come un modo efficiente per
# verificare che un numero sia effettivamente un quadrato perfetto.

# Prendo in input il potenziale "quadrato perfetto"
quadrato_perfetto = eval(input("Digita un numero: "))

# Intuizione: proviamo a controllare tutti i numeri naturali uno ad uno, e iteriamo
# fintanto che il quadrato del numero intero corrente risulta minore del numero digitato.
# Quando usciremo dal ciclo ci troveremo in due possibili situazioni:
#
#   1. Il quadrato è perfetto e quindi il numero intero raggiunto e' effettivamente
#   il numero che stiamo cercando, e quindi vale che intero * intero = quadrato_perfetto
#
#   2. Il quadrato NON è perfetto, e quindi intero*intero sarà necessariamente maggiore
#   di quadrato perfetto (perché se fosse minore ancora dentro al while e se fosse uguale
#   ricadiamo nel punto 1. sopracitato)
intero = 1
while intero * intero < quadrato_perfetto:
    intero = intero + 1

# Verifico se il numero raggiunto sia effettivamente la base del quadrato perfetto
if intero * intero == quadrato_perfetto:
    print(quadrato_perfetto, "e' un quadrato perfetto, ed e' il quadrato di", intero)
else:
    print(quadrato_perfetto, "non e' un quadrato perfetto")