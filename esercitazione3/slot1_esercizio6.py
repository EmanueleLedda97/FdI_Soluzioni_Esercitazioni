# Chiedere all’utente di digitare un numero intero ‘n’. Dopodiché, acquisire
# dall’utente ‘n’ numeri interi, e calcolare quali tra i numeri digitati
# sia il maggiore e quale il minore. Stampare infine i due valori.

n = eval(input("Quanti numeri digiterai? "))   # Chiedo l'input all'utente

maggiore = 0    # Creo una variabile per contenere il maggiore
minore = 0      # Creo una variabile per contenere il minore

# Itero n volte il ciclo
k = 0
while k < n:

    num_corrente = eval(input("Digita un numero: "))  # Chiedo in input il k-esimo numero

    # Se siamo dentro alla prima iterazione allora significa che è stato digitato UN SOLO numero.
    # Se è stato digitato un solo numero, allora significa che il maggiore tra tutti i numeri digitati
    # è proprio quel numero; ma anche il minore può essere solo quel numero. Quindi al primo giro il
    # maggiore ed il minore prendono il valore del primo numero digitato
    if k == 0:
        maggiore = num_corrente
        minore = num_corrente

    # Se il numero che è stato appena digitato è più piccolo del minor numero fino ad ora registrato,
    # allora significa che il più piccolo numero letto fino ad ora è proprio il numero corrente, e quindi
    # dobbiamo sostituire il valore della variabile 'minore' con il valore del nuovo numero digitato.
    if num_corrente < minore:
        minore = num_corrente

    # Similmente a quanto detto per il minore, se il numero che è stato appena digitato è più grande del
    # 'maggiore' registrato fino ad ora, allora significa che il numero corrente è il più grande numero
    # visto fino ad ora: quindi aggiorniamo il valore della variabile 'maggiore'.
    if num_corrente > maggiore:
        maggiore = num_corrente

    k = k + 1   # Incremento k

# Stampo il maggiore e il minore
print("Il numero maggiore e'", maggiore, "mentre il minore e'", minore)
