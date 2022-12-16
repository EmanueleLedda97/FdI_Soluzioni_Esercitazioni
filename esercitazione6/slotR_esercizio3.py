# Esercizio 3: Scrivere un programma che stampi in output la temperatura corporea di
# un paziente, ipotizzando che un generico paziente abbia la temperatura corporea
# che segue la distribuzione uniforme tra 35 e 38 gradi. Se il paziente ha la
# temperatura superiore a 37.1, segnalare che ha la febbre.

from random import uniform


# Creo la funzione utile a generare la temperatura del paziente in modo casuale
def misura_temperatura():
    temperatura_misurata = uniform(35, 38)
    return temperatura_misurata


# Misuro la temperatura del paziente (genero un numero casuale)
temperatura_paziente = misura_temperatura()

# Se la temperatura eccede i 37.1 allora avviso della febbre, altrimenti dico che è tutto ok.
if temperatura_paziente > 37.1:
    print("Hai la febbre a ", temperatura_paziente, "!")
else:
    print("Tutto ok, hai la temperatura a", temperatura_paziente)