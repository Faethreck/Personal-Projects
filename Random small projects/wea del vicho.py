def filtrar(original, eliminar):
   lista = []
   for i in original:
       if i not in eliminar:
           if i in lista:
               pass
           elif i not in lista:
                lista += [i]
                

   return lista

original = input()
eliminar = 
print(filtrar(original, eliminar))            