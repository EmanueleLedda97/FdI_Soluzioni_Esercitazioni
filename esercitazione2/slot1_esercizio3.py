# Scrivere il programma per la gestione della spesa dei biglietti del cinema.
# Il programma deve chiedere all’utente due numeri, rappresentanti la disponibilità
# economica in euro (ad esempio, 20.00), e la quantità di biglietti che vuole
# comprare (ad esempio 5 biglietti). Sapendo che il costo di un singolo biglietto
# del cinema è pari a 6.50 euro, se l’utente non ha abbastanza soldi per comprare
# il quantitativo di biglietti digitato il programma deve stampare la seguente
# stringa, sostituendo i puntini con le variabili opportune: “Mi dispiace, ma per
# comprare ... biglietti occorrono ... euro, e la tua disponibilita’ e’ solo ... euro”

costo_biglietto = 6.5   # Creo una variabile contenente il costo del biglietto
disponibilita = eval(input("Digita la tua disponibilita': "))       # Prendo in input la disponibilita
num_biglietti = eval(input("Quanti biglietti vuoi comprare? "))     # Prendo in input il numero di biglietti

spesa_totale = costo_biglietto * num_biglietti  # Calcolo la spesa totale da sostenere

# Se la spesa totale da sostenere è maggiore della propria disponibilità
# allora verrà stampato un messaggio di avvertimento
if spesa_totale > disponibilita:
    print("Mi dispiace, ma per comprare", num_biglietti, "biglietti occorrono",
          spesa_totale, "euro, e la tua  disponibilita' e' solo", disponibilita, "euro")    # Stampo il messaggio

# N.B. E' da notare che l'espressione poteva anche essere scritta al contrario come
# disponibilita < spesa_totale; ovviamente x<y e y>x sono due diseguaglianze equivalenti,
# e quindi è a nostra discrezione l'utilizzo dell'una piuttosto che l'altra


