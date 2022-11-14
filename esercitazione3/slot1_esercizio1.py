# Scrivere un programma che stampi un conto alla rovescia a partire da 10 fino
# a ad arrivare a 0 (decidete voi se includere lo zero oppure no).
# Dopo aver ultimato il conto alla rovescia stampare il messaggio “Buon anno!”

# Creo un contatore che parte da 10, con l'intento di utilizzarlo decrementandolo,
# e quindi facendo k = k - 1 dentro al ciclo while
k = 10

# Finché k rimane positivo, continuo ad iterare il ciclo.
while k > 0:
    print(k)        # Stampo k in quanto k contiene il valore che viene progressivamente decrementato
    k = k - 1       # Decremento k

# Alla fine del programma stampo "Buon Anno!"
print("Buon Anno!")

# N.B. Occhio che qui stiamo ragionando "al contrario" rispetto agli esercizi precedenti; stiamo
# decrementando un contatore fino a un valore di limite inferiore (finché k non è PICCOLO quanto un dato numero X),
# anziché incrementarlo fino a un valore limite superiore (finché k non è grande quanto un dato numero X).
# Tuttavia, similmente all'esempio alternativo dell'esercizio guidato, noi potremmo iterare tra 0 e 10,
# e cambiare solo il messaggio nella print anziché cambiare le condizioni di incremento, controllo del ciclo e
# inizializzazione del contatore. Questa soluzione analoga risulta però meno intuitiva, ma comunque interessante
# da analizzare per capirne il funzionamento:
#
# k = 0
# while k < 10:
#     print(10 - k)
#     k = k + 1
# print("Buon Anno!")
