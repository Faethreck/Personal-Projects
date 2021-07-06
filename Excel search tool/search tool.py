# SEARCH TOOL FOR EXCEL
import openpyxl
from openpyxl import load_workbook

program = True

workbook = load_workbook(filename='Book1.xlsx', data_only=True)
# month worksheet variables
enero =  workbook['ENERO']
febrero =  workbook['FEBRERO']
marzo = workbook['MARZO']
abril =  workbook['ABRIL']
mayo = workbook['MAYO']
junio =  workbook['JUNIO']
julio =  workbook['JULIO']
agosto =  workbook['AGOSTO']
septiembre = workbook['SEPTIEMBRE']
octubre =  workbook['OCTUBRE']
noviembre =  workbook['NOVIEMBRE']
diciembre =  workbook['DICIEMBRE']
#####################################
# months variables list
meses = [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre]
###############################################################################################################
# search function
while program == True:
    # rut a buscar
    rut = str(input("RUT: "))
    #########################
    # funcion de buscador de horas y sueldo en el mes
    def search(rut, mes):
        if mes == 'enero':
            mes = enero
        elif mes == 'febrero':
            mes = febrero
        elif mes == 'marzo':
            mes = marzo
        elif mes == 'mayo':
            mes = mayo        
        elif mes ==  'abril':
            mes = abril
        elif mes == 'agosto':
            mes = agosto
        elif mes == 'junio':
            mes = junio
        elif mes == 'julio':
            mes = julio
        elif mes == 'septiembre':
            mes = septiembre
        elif mes == 'octubre':
            mes = octubre
        elif mes == 'noviembre':
            mes = noviembre
        elif mes ==  'diciembre':
            mes = diciembre
        print(mes)

        counter = 4
        rut2 = mes['C%d' % counter].value
        column = mes['C']
        for row  in column:
            global total_horas, total_sueldos, valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10, valor11, valor12, valor1_, valor2_, valor3_, valor4_, valor5_, valor6_, valor7_, valor8_, valor9_, valor10_, valor11_, valor12_
            counter += 1  
            rut2 = row.value

            if rut == rut2:
                    # normal = O / sep = T / proretencion = D
                    counter = counter -4            
                    horas = mes['O%d' % counter].value             
                    sueldo = mes['AT%d' % counter].value
                    print('El rut es: ' + str(rut))
                    print('EL sueldo del mes es: ' + str(sueldo))
                    print('Las horas del mes son: ' + str(horas))
                    if horas == None:
                        horas = 0
                    if sueldo == None:
                        sueldo = 0
                             
                    #print('El rut es: ' + str(rut))
                    #print('EL sueldo del mes es: ' + str(sueldo))
                    #print('Las horas del mes son: ' + str(horas))

                    if mes == enero:
                        valor1 = int(horas)                          
                        valor1_ = int(sueldo)
                            
                    elif mes == febrero:
                        
                        valor2 = int(horas)
                        valor2_ = int(sueldo)
                   
                    elif mes == marzo:
                        
                        valor3 = int(horas)
                        valor3_ = int(sueldo)
        
                    elif mes == mayo:
                        
                        valor4 = int(horas)
                        valor4_ = int(sueldo)
                    
                    elif mes ==  abril:
                        
                        valor5 = int(horas)
                        valor5_ = int(sueldo)
                    
                    elif mes == agosto:
                        
                        valor6 = int(horas)
                        valor6_ = int(sueldo)
                    
                    elif mes == junio:
                        
                        valor7 = int(horas)
                        valor7_ = int(sueldo)
                   
                    elif mes == julio:
                        
                        valor8 = int(horas)
                        valor8_ = int(sueldo)
                    
                    elif mes == septiembre:
                       
                        valor9 = int(horas)
                        valor9_ = int(sueldo)
                    

                    elif mes == octubre:
                        
                        valor10 = int(horas)
                        valor10_ = int(sueldo)
                    
                    
                    elif mes == noviembre:
                       
                        valor11 = int(horas)
                        valor11_ = int(sueldo)
                    

                    elif mes ==  diciembre:
                       
                        valor12 = int(horas)
                        valor12_ = int(sueldo)                
                                                        
                    break            
            elif rut != rut2:
                    horas = None
                    sueldo = None
                    if horas == None:
                        horas = 0
                    if sueldo == None:
                        sueldo = 0

                    if mes == enero:
                        
                        valor1 = int(horas)                          
                        valor1_ = int(sueldo)
                            
                    elif mes == febrero:
                        
                        valor2 = int(horas)
                        valor2_ = int(sueldo)
                   
                    elif mes == marzo:
                        
                        valor3 = int(horas)
                        valor3_ = int(sueldo)
        
                    elif mes == mayo:
                        
                        valor4 = int(horas)
                        valor4_ = int(sueldo)
                    
                    elif mes ==  abril:
                        
                        valor5 = int(horas)
                        valor5_ = int(sueldo)
                    
                    elif mes == agosto:
                        
                        valor6 = int(horas)
                        valor6_ = int(sueldo)
                    
                    elif mes == junio:
                       
                        valor7 = int(horas)
                        valor7_ = int(sueldo)
                   
                    elif mes == julio:
                        
                        valor8 = int(horas)
                        valor8_ = int(sueldo)
                    
                    elif mes == septiembre:
                        
                        valor9 = int(horas)
                        valor9_ = int(sueldo)
                    

                    elif mes == octubre:
                        
                        valor10 = int(horas)
                        valor10_ = int(sueldo)
                    
                    
                    elif mes == noviembre:
                       
                        valor11 = int(horas)
                        valor11_ = int(sueldo)
                    

                    elif mes ==  diciembre:
                        
                        valor12 = int(horas)
                        valor12_ = int(sueldo)                
    #  pregunta para calcular todos los meses                                                                                               
    question = input('Quieres calcular todos los meses? ')
    ######################################################
    # si la respuesta es 'si, el programa loopea sobre la lista de variables de los meses por cada mes y activa la funcion search() para obtener los valores #
    if question == 'si':
        for i in meses:
            search(rut, i)
        total_horas = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9 + valor10 + valor11 + valor12
        total_sueldos = valor1_ + valor2_ + valor3_ + valor4_ + valor5_ + valor6_ + valor7_ + valor8_ + valor9_ + valor10_ + valor11_ + valor12_
        print('El total de horas es: ' + str(total_horas))
        print('El total de sueldos es: ' + str(total_sueldos))
    ####################################################################################################################################################
    elif question == 'no':
        answer = input('Que mes quieres leer? ')
        print(search(rut,answer))          
       
    question = input("Quieres hacer otra busqueda? ")

    if question == 'si':
        program = True
    elif question == 'no':
        program = False
    else:
        program = False