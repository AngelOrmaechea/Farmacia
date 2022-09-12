import numeros

print("Bienvenido a la farmacia Di Stefano")
def inicio():

    print("Elige el turno que quieras sacar.")

    while True:
        try:
            rubro = input("P - Perfumeria, F - Farmacia, C - Cosmeticos").lower()
            ["f", "c", "p"].index(rubro)
        except ValueError:
            print("Por favor, elija una de las opciones dadas")
        else:
            break

    numeros.decorar(rubro)


def bucle(comienzo):
    print("¿Desea sacar un turno?")
    try:
        sino = input("si/no").lower()
        ["si", "no"].index(sino)
    except ValueError:
        print("La respuesta debe ser: SI o NO")
    else:
        while sino == "si":
            inicio()


bucle(inicio())
