# Esercizio 3.1: Definire la funzione ‘crea_vettore3D’ che chieda all’utente di
# digitare tre numeri reali e che costruisca (e restituisca) un dizionario
# avente come chiavi ‘x’, ‘y’ e ‘z’ e avente come valori i tre numeri digitati
# dall’utente.
def crea_vettore3D():
    vettore3D = {
        'x': eval(input("Digita la coordinata x: ")),
        'y': eval(input("Digita la coordinata y: ")),
        'z': eval(input("Digita la coordinata z: "))
    }
    return vettore3D


# Esercizio 3.2: Creare la funzione ‘norma3D_euclidea’ che prende in ingresso
# un dizionario di tipo ‘vettore’ e restituisca la norma euclidea del vettore.
def norma3D_euclidea(vett):
    norma3D = (vett['x'] ** 2 + vett['y'] ** 2 + vett['z'] ** 2) ** 0.5
    return norma3D


# Esercizio 3.3: Creare due vettori, ‘v1’ e ‘v2’ tramite la funzione
# ‘crea_vettore3D’, e determinare quale tra i due ha la norma maggiore
# tramite la funzione ‘norma3D_euclidea’.
v1 = crea_vettore3D()
v2 = crea_vettore3D()

# Qui decido di gestire il caso in cui la norma sia uguale (nel testo non è richiesto esplicitamente)
if norma3D_euclidea(v1) != norma3D_euclidea(v2):
    if norma3D_euclidea(v1) > norma3D_euclidea(v2):
        print("Il primo vettore ha la norma maggiore")
    else:
        print("Il secondo vettore ha la norma maggiore")
else:
    print("I due vettori hanno la norma uguale")


# Esercizio 3.4: Creare la funzione ‘scala_vettore’ che prende in ingresso
# un dizionario di tipo vettore, uno scalare ‘c’ e restituisca il
# vettore scalato.
def scala_vettore(vettore3D, c):
    vettore3D_scalato = {
        'x': vettore3D['x'] * c,
        'y': vettore3D['y'] * c,
        'z': vettore3D['z'] * c
    }
    return vettore3D_scalato
