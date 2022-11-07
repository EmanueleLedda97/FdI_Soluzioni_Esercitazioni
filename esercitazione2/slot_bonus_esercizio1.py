# Chiedere all’utente di digitare tre numeri rappresentati le
# lunghezze di tre segmenti, e verificare (stampando un messaggio)
# se i tre segmenti possono formare un triangolo (ciò è possibile se
# e solo se ciascuna delle tre lunghezze è minore della somma delle altre due.
# Se è possibile sistemare i tre segmenti per formare un triangolo,
# verificare (stampando un messaggio) se si tratta di un triangolo equilatero,
# isoscele o scaleno. Verificare anche (stampando un messaggio) se
# l’eventuale triangolo è anche un triangolo rettangolo (avviene quando il
# quadrato di uno dei tre lati è uguale alla somma dei quadrati degli altri due).

s1 = eval(input("Digitare la lunghezza del primo segmento: "))
s2 = eval(input("Digitare la lunghezza del secondo segmento: "))
s3 = eval(input("Digitare la lunghezza del terzo segmento: "))

# Se anche solo uno dei tre segmenti è maggiore o uguale alla somma degli altri
# due, o se un segmento è negativo, allora stampiamo un messaggio di errore
if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2 or s1 < 0 or s2 < 0 or s3 < 0:
    print("Mi dispiace, ma non e' possibile formare un triangolo")
else:
    # Se il primo è uguale al secondo e anche al terzo segmento, allora è equilatero
    if s1 == s2 and s1 == s3:
        print("Il triangolo e' equilatero")
    else:
        # Se invece sono tutti e tre diversi tra loro allora è scaleno
        if s1 != s2 and s1 != s3 and s2 != s3:
            print("Il triangolo e' scaleno")
        # Per esclusione, se non è né scaleno né equilatero dev'essere isoscele
        else:
            print("Il triangolo e' isoscele")

        # Se inoltre il quadrato di un lato è uguale alla somma dei quadrati dell'altro
        # allora il triangolo è anche rettangolo. Ciò avviene solo per triangoli scaleni e isosceli
        if s1**2 == s2**2 + s3**2 or s2**2 == s1**2 + s3**2 or s3**2 == s1**2 + s2**2:
            print("Inoltre, il triangolo e' anche rettangolo")

# N.B. La condizione per verificare che il triangolo sia rettangolo può esser messa sia
# internamente all'else dopo aver escluso i triangoli equilateri, sia all'altezza del primo if.
# Semanticamente, inserirlo internamente fa saltar subito all'occhio che è una condizione
# che può verificarsi SOLO quando il triangolo non è equilatero.
