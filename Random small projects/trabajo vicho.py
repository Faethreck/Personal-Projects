#Listas
características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]


amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]
#Fin de listas


#Funciones
def obtener_valor_característica(características, buscada):
    for caracter, puntos in  características:       
        if caracter == buscada:
            return puntos
        
    return 0


def puntaje_amigo(amigo, características):
    _, personalidad = amigo
    print(personalidad)
    i = 0
    suma = 0
    while i < len(personalidad):
        suma += obtener_valor_característica(características, personalidad[i])
        i += 1
    
    return suma

#Fin de funciones


######################################################
#Programa
######################################################

#Lista de puntajes
lista = []
nombres = []
i = 0

while i < len(amigos):
    nombre, carac = amigos[i]
    if "lolero" in carac:
        puntos= puntaje_amigo(amigos[i], características)
        print(puntos)
        lista.append(puntos)
        nombres.append(nombre)   
    i += 1
###################################################################

print(lista,nombres)


j = 0
flag = False
combinacion = []

for rango in range(len(lista+ nombres)):
        for i in nombres:
            if flag == False:
                if i in combinacion:
                    pass
                elif i not in combinacion:
                    combinacion.append(i)
                    flag = True
                    j += 1
        for i in lista:
            if flag == True:
                if i in combinacion:
                    pass
                elif i not in combinacion:
                    combinacion.append(i)
                    flag = False
                    j += 1
    
        
print(combinacion)
sorteada = []       

for  in combinacion:
    print(i)
    if i == str:    
        sorteada.append(i)
    elif i == int:
        sorteada.append(i)

print(sorteada)

