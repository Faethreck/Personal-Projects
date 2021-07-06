tablero = [
['-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-'],
['0','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-'],
['-','-','-','0','-','-','-','-','-'],
['-','-','-','0','0','-','-','-','-'],
['-','-','-','0','0','-','-','-','-']
]

barcos = [
[2, 1, 4, 8],
[1, 2, 0, 3],
[3, 1, 3, 6]
]


def disparo(tablero, barcos, fila, columna):
    for linea in tablero:
        for casilla in linea:
            if casilla == '-':
                for i in barcos:
                    if fila == i[2] and columna == i[3]:         
                        linea[columna] = "O"
                    elif fila != i[2] and columna != i[3]:
                        linea[columna] = " "
        print(tablero)
        return casilla



print(disparo(tablero,barcos, 0, 3))