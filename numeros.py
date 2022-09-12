#generadores
#decoradores
def decorar(turno):
    print("Su turno es: ")
    if turno == "p":
        print("P -", next(p))
    elif turno == "f":
        print("F -", next(f))
    elif turno == "c":
        print("C -", next(c))
    print("Aguarde pacientemente.")


def perfum():
    for n in range(1, 347896):
        yield n


def farmac():
    for n in range(1, 347896):
        yield n


def cosmet():
    for n in range(1, 347896):
        yield n


p = perfum()
f = farmac()
c = cosmet()


