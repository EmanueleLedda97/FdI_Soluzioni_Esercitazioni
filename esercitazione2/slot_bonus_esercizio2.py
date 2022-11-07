# Chiedere all’utente di digitare 4 numeri tutti diversi tra loro.
# Se ci sono coppie di numeri uguali tra quelli digitati segnalarlo
# tramite un messaggio in output, altrimenti stampare i quattro
# numeri dal più piccolo al più grande.

# N.B. Questo esercizio bonus risulta abbastanza complesso per essere risolto
# con le conoscenze attuali (senza usare tipi iterabili e istruzioni d'iterazione).
# La soluzione seguente è solo una delle tante possibili, ed è quella che, ad avviso
# del tutor, risulta la più "elegante" e "pulita" da applicare per l'ordinamento di
# 4 variabili mediante l'utilizzo di semplici istruzioni condizionali, ma sono ovviamente
# possibili tante soluzioni altrettanto buone.

# Prendo in input i quattro numeri
n1 = eval(input("Digita il primo numero: "))
n2 = eval(input("Digita il secondo numero: "))
n3 = eval(input("Digita il terzo numero: "))
n4 = eval(input("Digita il quarto numero: "))

if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("Mi dispiace, ma ci sono coppie uguali tra loro")
else:
    # Scambio (se necessario) i valori delle variabili n1 ed n2:
    # così facendo mi assicuro che valga l'uguaglianza n1 < n2
    if n2 < n1:
        swap = n1   # Salvo il valore di n1 dentro la variabile swap
        n1 = n2     # Assegno ad n1 il valore di n2
        n2 = swap   # Assegno ad n2 il vecchio valore di n1 (contenuto in swap)

    # Scambio (se necessario) i valori delle variabili n3 ed n4:
    # così facendo mi assicuro che valga l'uguaglianza n3 < n4
    if n4 < n3:
        swap = n3   # Salvo il valore di n3 dentro la variabile swap
        n3 = n4     # Assegno ad n3 il valore di n4
        n4 = swap   # Assegno ad n4 il vecchio valore di n3 (contenuto in swap)

    # Sappiamo che n1 < n2 e che n3 < n4.
    # Questo significa che il primo da stampare sarà o n1 o n3, in quanto sono i più piccoli.
    # Controllo chi dei due è il minore come primo controllo, per sapere chi stampare per primo.
    if n1 < n3:
        # Fin qui n1 è il minore.
        # Se n2 < n3 allora logica impone che n1 < n2 < n3 < n4
        if n2 < n3:
            print(n1, n2, n3, n4)
        else:
            # Se viceversa (else) n3 < n2, allora devo controllare il minore tra n2 ed n4
            if n2 < n4:
                print(n1, n3, n2, n4)
            else:
                print(n1, n3, n4, n2)

    else:
        # Fin qui n3 è il minore.
        # Se n4 < n1 allora logica impone che n3 < n4 < n1 < n2
        if n4 < n1:
            print(n3, n4, n1, n2)
        else:
            # Se viceversa (else) n1 < n4, allora devo controllare il minore tra n2 ed n4
            if n2 < n4:
                print(n3, n1, n2, n4)
            else:
                print(n3, n1, n4, n2)



