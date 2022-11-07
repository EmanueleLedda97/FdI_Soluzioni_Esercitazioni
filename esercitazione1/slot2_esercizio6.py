# Scrivere un programma che chieda all’utente un importo espresso in Euro,
# lo converta in dollari statunitensi (assumendo il tasso di cambio
# 1 euro = 1,15 dollari statunitensi), e stampi il seguente messaggio:
# “L’importo di ... euro equivale a ... USD.”

importo_euro = eval(input("Digita un importo in euro: "))   # Prendo in input l'importo in euro
importo_usd = importo_euro * 1.15   # Calcolo l'importo in dollari secondo la valuta riportata nel testo
print("L'importo di", importo_euro, "euro equivale a", importo_usd, "USD")  # Stampo il messaggio
