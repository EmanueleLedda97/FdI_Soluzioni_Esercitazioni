# Verificare (stampando un messaggio) se un numero digitato in input sia pari o dispari.

# Ripasso sui criteri di divisibilità: un numero N è divisibile per M se può essere scritto nella forma:
#   N = M*Q + R, con R=0
# In sostanza, possiamo dividere N per M se il resto della divisione intera tra N ed M da' zero.
# Ricordiamo anche che un numero è detto "pari" quando è divisibile per 2.
# Questo significa che per controllare se un numero è pari occorrerà controllare se quel numero
# è divisibile per 2, e ciò significa verificare che il resto della divisione intera tra N e 2 dia zero.
# In termini pratici, in python usiamo l'operatore "modulo" per calcolare il resto della divisione,
# e quindi l'espressione condizionale da utilizzare per verificare la parità è la seguente:
#   N % 2 == 0

numero = eval(input("Digitare un numero: "))    # Prendo in input un numero

# Se il resto della divisione intera tra il numero e 2 equivale a zero, allora
# significa che il numero e pari e lo comunico con un messaggio; altrimenti significa
# che è dispari e lo comunico con un altro messaggio
if numero % 2 == 0:
    print("Il numero e' pari")      # Stampo il messaggio di verificata parità (nell'if)
else:
    print("Il numero e' dispari")   # Stampo il messaggio di verificata disparità (nell'esle)
