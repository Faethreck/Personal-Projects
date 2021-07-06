
nota_presentacion = int(input("inserte nota presentacion: ")) * 0.1


def calculador(nota_presentacion):
    valor1 = nota_presentacion * 0.7
    notanecesaria = ((valor1 - 4) / 0.3)

    if notanecesaria < 0:
        notanecesaria = notanecesaria * - 1
    
    print(notanecesaria)

calculador(nota_presentacion)