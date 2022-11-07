# Scrivere un programma per la navigazione marittima.
# Il programma deve chiedere all’utente di digitare due punti su una
# mappa (un numero per la coordinata x e uno per la y, per ognuno
# dei due punti), che si riferiscono alle coordinate di due isole
# in km, una di partenza e una d’arrivo.
# Sapendo che si dispone di una nave con un’autonomia di 500 km,
# calcolare la distanza tra le due isole e stampare il messaggio
# "Viaggio consentito" se la distanza non supera l’autonomia
# della nave, altrimenti stampare il messaggio:
# "Viaggio non consentito, la nave non dispone di ... km di autonomia"

autonomia = 500.0   # Variabile contenente l'autonomia della nave in km

# Prendo le coordinate dei due punti: (x,y) di partenza e (x,y) d'arrivo
x_partenza = eval(input("Digita la coordinata x dell'isola di partenza: "))
y_partenza = eval(input("Digita la coordinata y dell'isola di partenza: "))
x_arrivo = eval(input("Digita la coordinata x dell'isola d'arrivo: "))
y_arrivo = eval(input("Digita la coordinata y dell'isola d'arrivo: "))

# Calcolo la distanza euclidea tra i due punti
distanza = ((x_partenza - x_arrivo) ** 2 + (y_partenza - y_arrivo) ** 2) ** 0.5

# Se la distanza eccede l'autonomia stampiamo il messaggio d'avviso
if distanza > autonomia:
    print("Viaggio non consentito, la nave non dispone di", distanza, "km di autonomia")
else:
    print("Distanza da percorrere ", distanza, "km. Viaggio consentito")


# N.B. è interessante notare che possiamo fare la radice quadrata (o qualsiasi altra radice)
# sfruttando le proprietà dei radicali. Più avanti vedremo che potremo utilizzare delle funzioni
# per il calcolo di tante funzioni matematiche come seno, coseno e appunto anche radice quadrata,
# ma l'operatore di elevazione a potenza di python ci permette di calcolare i valori dei radicali
# senza la necessità di ricorrere a funzioni particolari (che tratteremo più avanti)
