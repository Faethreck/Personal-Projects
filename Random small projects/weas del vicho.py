diccionario_vacio = {55: 2, 40: 1, 18: 3}
contador= []
for key in diccionario_vacio:
    baul = diccionario_vacio[key]
    contador.append(baul)
    contador.sort()
    contador.reverse()
    
for numero in contador:
    if numero == diccionario_vacio[key]:
        print(str(key) + ' anios = ' + str(numero))
print("final: ",contador)



        
