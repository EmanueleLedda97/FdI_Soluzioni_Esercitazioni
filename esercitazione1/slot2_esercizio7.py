# Scrivere un programma che chieda all’utente l’anno della propria nascita,
# calcolare l’età dell’utente e stampare a video il messaggio:
# “Anno di nascita …, eta’ attuale …”.

anno_attuale = 2022     # Creo una variabile per salvare l'anno attuale
anno_nascita = eval(input("Qual e' il tuo anno di nascita? "))  # Prendo in input l'anno di nascita
eta = anno_attuale - anno_nascita   # Calcolo l'eta' sulla base dell'anno attuale e dell'anno di nascita

print("Anno di nascita", anno_nascita, "eta' attuale", eta)     # Stampo il messaggio
