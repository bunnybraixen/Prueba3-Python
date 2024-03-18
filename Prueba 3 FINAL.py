import numpy as np
import os


matriz_autos = np.array([['Lista', 'De', 'Automobiles', 'Automotora', 'Conejo', 'Autos' ],['Patente', 'Marca','Modelo', 'Año', 'Valor', 'Estado Venta'] ])
fila = 0


print (matriz_autos)
def guardar():
    print("Ingrese la patente del auto (6 caracteres)")
    patente = str(input())
    if len(patente) == 6:
        print ("Ingrese marca del auto (3 caracteres)")
        marca = str(input())
        if len(marca) == 3:
            print ("Ingrese modelo del auto (3 caracteres)")
            modelo = str(input())
            if len(modelo) == 3:
                print ("Ingrese año del vehiculo (Solo se aceptan autos sobre el 2000)")
                año = int(input())
                if año > 2000 and año <= 2023:
                    print ("Ingrese el valor del auto (Minimo 500.000)")
                    valor = int(input())
                    if valor >=500000:
                        matriz_nueva = np.array([[patente, marca, modelo, int(año), str(valor), 'NO VENDIDO' ],['Patente', 'Marca','Modelo', 'Año', 'Valor', 'Estado Venta'] ])
                        return matriz_nueva
                        
                    else:

                        print("El valor ingresado no cumple con el minimo, vuelva a intentarlo")    
                        input ("Presione enter para continuar")
                        return False
                else:

                    print("El año del vehiculo no esta en un rango valido, vuelva a intentarlo")     
                    input ("Presione enter para continuar")
                    return False
            else:
                print("El modelo ingresada no cumple con los caracteres necesarios, vuelva a intentarlo")     
                input ("Presione enter para continuar")
                return False
        else:
            print("La marca ingresada no cumple con los caracteres necesarios, vuelva a intentarlo")     
            input ("Presione enter para continuar")
            return False
    else:
        print("La patente ingresada no cumple con los caracteres necesarios, vuelva a intentarlo")        
        input ("Presione enter para continuar")
        return False



menu = 1
while menu == 1:
    os.system('cls')
    print ("Bienvenido a Automotora Conejo")
    print ("(1) Guardar Automovil")
    print ("(2) Buscar Automovil")
    print ("(3) Listar Automoviles")
    print ("(4) Imprimir Compraventa")
    print ("(5) Salir")
    print ("Ingrese una opcion:")
    opcion = input()
    if opcion == '1':
        matriz = guardar()
        if matriz == False:
            pass
        else:
            os.system('cls')
            matriz_autos = np.concatenate ((matriz_autos, matriz), axis=0)
            print ("El auto ha sido ingresado con exito")
            input ("Presione enter para continuar")

            
    elif opcion == '2':
        print ("Seleccione la patente del Automovil que se desea buscar")
        patente = input()
        os.system('cls')
        check = 0
        if len(patente) == 6:
            for i in range(len(matriz_autos)):
                if matriz_autos[i,0] == patente:
                    print ("Patente del auto:", matriz_autos[i,0])
                    print ("Marca del auto:", matriz_autos[i,1])
                    print ("Modelo del auto:", matriz_autos[i,2])
                    print ("Año del auto:", matriz_autos[i,3])
                    print ("Valor del auto:", matriz_autos[i,4])
                    años = 2023 - int(matriz_autos[i,3])
                    print ("Años de fabricacion: ", años)
                    print ("Estado del auto: ", matriz_autos[i,5])
                    
                    check=1
            if check == 0:
                print ("La patente ingresada no pertenece a ningun auto")
            input("Presione enter para continuar")
                
        else:
            print("La patente ingresada no cumple con los caracteres necesarios, vuelva a intentarlo")        
            input ("Presione enter para continuar")
    elif opcion == '3':
        print ("Esta es la lista actual de autos")
        print (matriz_autos)
        input ("Presione enter para continuar")
    elif opcion == '4':
        print ("Seleccione la patente del Automovil que se desea vender")
        patente = input()
        os.system('cls')
        check = 0
        if len(patente) == 6:
            for i in range(len(matriz_autos)):
                if matriz_autos[i,0] == patente:
                    if matriz_autos[i,0] == patente:
                        if matriz_autos[i,5] == 'NO VENDIDO':
                            print ("CONTRATO DE COMPRAVENTA")
                            numero = np.random.randint(low=1000, high=50000)
                            print ("Numero de contrato:", numero)
                            print ("Patente del auto:", matriz_autos[i,0])
                            print ("Marca del auto:", matriz_autos[i,1])
                            print ("Modelo del auto:", matriz_autos[i,2])
                            print ("Año del auto:", matriz_autos[i,3])
                            print ("Valor del auto:", matriz_autos[i,4])
                            años = 2023 - int(matriz_autos[i,3])
                            print ("Años de fabricacion: ", años)
                            matriz_autos[i,5] = 'VENDIDO'
                            print ("Estado del auto: ", matriz_autos[i,5])
                            check = 1
                        else:
                            print ("El auto que se ha ingresado ya ha sido vendido")  
                            check = 1                     

            if check == 0:
                print ("La patente ingresada no pertenece a ningun auto")
            input ("Presione enter para continuar")

                    
        else:
            print("La patente ingresada no cumple con los caracteres necesarios, vuelva a intentarlo")        
            input ("Presione enter para continuar")
    elif opcion == '5':
        menu=5555555555555
        print("Gracias por usar nuestra aplicacion")        
        input ("Presione enter para salir")
    else: 
        print("La opcion ingresada no es valida, vuelva a intentarlo")        
        input ("Presione enter para continuar")

    
