# Scrivere un programma che acquisisca due numeri naturali, sottragga il più
# piccolo dal più grande e stampi il risultato nella shell.

# Prendo in input i due numeri
num1 = eval(input("Digita il primo numero: "))
num2 = eval(input("Digita il secondo numero: "))

# Se il primo numero è più piccolo allora lo sottraggo dal secondo
if num1 < num2:
    sottrazione = num2 - num1
else:
    sottrazione = num1 - num2   # Altrimenti sottraggo il secondo dal primo

# Stampo in output il risultato
print("Il risultato della sottrazione e': ", sottrazione)