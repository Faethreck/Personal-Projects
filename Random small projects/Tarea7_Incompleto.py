##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################

def disparo(tablero, barcos, fila, columna):
    casilla = tablero[fila][columna]
    for barco in barcos:
        print(barco)
        posicion_x = []
        posicion_y = []    
        direccion = barco[1]
        rango = barco[0]
        if direccion == 1:
            for y in range(rango):
                print(y)
                num = barco[2] + y
                posicion_y.append(num)
                
            posicion_x.append(barco[3])
            
            
        if direccion == 2:
            for x in range(rango):
                num = barco[3] + x
                posicion_x.append(num)
            posicion_y.append(barco[2])
            
        if casilla == "-":
            if fila in posicion_x and columna in posicion_y:
                print('fila%d' % fila)
                print('columna%d' % columna)
                print(posicion_x)
                print(posicion_y)
                tablero[fila].pop(columna)
                tablero[fila].insert(columna,'O')
            if fila not in posicion_x or columna not in posicion_y:
                print('fila%d' % fila)
                print('columna%d' % columna)
                tablero[fila].pop(columna)
                tablero[fila].insert(columna,' ')
                
                    
                
        

    # Desarrolle aquí su código para la función


def destruidos(tablero, barcos):
    
    puntos = 0
    destroyed = 5   
    for barco in barcos:
        posicion_x = []
        posicion_y = []    
        direccion = barco[1]
        rango = barco[0]

        if direccion == 1:
            
            for y in range(rango):
                num = barco[2] + y
                posicion_x.append(num)
            posicion_y.append(barco[3])

        elif direccion == 2:
            for x in range(rango):
                num = barco[3] + x
                posicion_y.append(num)
            posicion_x.append(barco[2])
        for lineas in tablero:
            for casilla in lineas:
                if casilla == "O":
                    puntos += 1
                    if puntos == rango:
                        destroyed += 1
        return 0
                    
                        
            
        
    

    # Desarrolle aquí su código para la función








# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 1



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
