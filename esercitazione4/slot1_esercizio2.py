# Scrivere un programma che acquisisca la lunghezza del lato di un quadrato
# e del lato di un triangolo equilatero, e determini se le due figure hanno
# la stessa area e/o lo stesso perimetro.

# Prendo in input il lato del quadrato e del triangolo
lato_quadrato = eval(input("Digita il lato del quadrato: "))
lato_triangolo = eval(input("Digita il lato del triangolo: "))

# Calcolo area e perimetro del quadrato
area_quadrato = lato_quadrato * lato_quadrato
perimetro_quadrato = lato_quadrato * 4

# Calcolo area e perimetro del triangolo: qui mi serve calcolare prima l'altezza
altezza_triangolo = lato_triangolo * (3 ** 0.5) / 2         # H = L * radice(3) / 2
area_triangolo = (lato_triangolo * altezza_triangolo) / 2
perimetro_triangolo = lato_triangolo * 3

# Controllo se l'area delle due figure è uguale
print("Area quadrato:", area_quadrato, "Area triangolo: ", area_triangolo)
if area_quadrato == area_triangolo:
    print("Quadrato e triangolo hanno la stessa area")

# Controllo se il perimetro delle due figure è uguale
print("Perimetro quadrato:", perimetro_quadrato, "Perimetro triangolo: ", perimetro_triangolo)
if perimetro_quadrato == perimetro_triangolo:
    print("Quadrato e triangolo hanno lo stesso perimetro")
