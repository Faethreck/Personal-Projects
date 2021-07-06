diccionario_vacio = {55: 1, 40: 1, 18: 5}
contador= []
for key in diccionario_vacio:
    baul = diccionario_vacio[key]
    contador.append(baul)
    contador.sort()
    contador.reverse()
print("final: ",contador)

for numero,index in enumerate(contador):
    for key_2 in diccionario_vacio:
        if index == diccionario_vacio[key_2]:
            print(str(key_2) + " años: " + str(index) + " personas")
            diccionario_vacio[key_2] = "listo"
            