import os

nH=[]
Name=[]
nD=[]
cdOr=[]
T=0
Tp=[]
fP=[]
NumP=[]
h1=1000
h2=1500
h3=500

#MENÚ
print("---BIENVENIDO---")
while True:
    print("="*40)
    print("1. Registro\n2.Búsqueda\n3.Reportes\n4.Modificaciones\n5.Eliminar\n6.Salir ")
    print("="*40)
    op=int(input("\nElige una opcion: "))
    print("="*48)

    match op:
        #REGISTRO
        case 1:
           print("===REGISTRO===")
           opr=input("¿Para cuantas personas necesita su habitacion? (1 persona, 2 personas y +3 personas): ")
           #OPCIONES DE HABITACION
           match opr:
               case '1':
                   #NUMERO DE HABITACIÓN
                   h=int(input("Ingrese el número de habitación (1-3): "))
                   #VALIDACION DE HABITACION
                   if h in nH:
                       print(f"La habitacion {h} ya esta ocupada")
                       continue
                   #NOMBRE
                   n=input("Ingrese el nombre: ")
                   #NUMERO DE DIAS
                   D=int(input("Ingrese el número de Días: "))
                   #CIUDAD DE ORIGEN
                   cor=(input("Ingrese la ciudad de origen del huesped: " ))
                   #TOTAL A PAGAR
                   T=D*h1
                   #FORMA DE PAGO
                   fpago=input("Ingrese la forma de pago: ")

                   #SE AGREGAN A LAS LISTAS
                   fP.append(fpago)
                   Tp.append(T)
                   cdOr.append(cor)
                   nD.append(D)
                   Name.append(n) 
                   nH.append(h)
                   NumP.append(1)
                  
               case '2' :
                   #NUMERO DE HABITACIÓN
                   h=int(input("Ingrese el número de habitación (4-6): "))
                   #VALIDACION DE LA HABITACION
                   if h in nH:
                       print(f"La habitación {h} est ocupada")
                       continue 
                   #NUMERO DE HUESPEDES
                   num_pers=int(input("Ingrese el numero de huespedes: "))
                   #NOMBRE DEL TITULAR
                   n=input("Ingrese el nombre: ")
                   #CIUDAD DE ORIGEN
                   cor=input("Ingrese la ciudad de origen del huesped: ")
                   #NUMERO DE DIAS
                   D=int(input("Ingrese el número de Días: "))
                   #TOTAL A PAGAR
                   T=D*h2
                   #FORMA DE PAGO
                   fpago=input("Ingrese la forma de pago: ")

                   #SE AGREGAN A LAS LISTAS
                   nH.append(h)
                   Name.append(n)
                   nD.append(D)
                   cdOr.append(cor)
                   Tp.append(T)
                   fP.append(fpago)
                   NumP.append(num_pers)
               
               case '+3':
                   #NUMERO DE HABITACIÓN
                   h=int(input("Ingrese el número de habitación (7-9): "))
                   #VALIDACION DE HABITACION
                   if h in nH:
                       print(f"La habitación {h} esta ocupada")
                       continue
                   #NUMERO DE HUESPEDES
                   num_pers=int(input("Ingrese el numero de huespedes: "))
                   #NOMBRE DEL titular
                   n=input("Ingrese el nombre del titular: ")
                   #CIUDAD DE ORIGEN
                   cor=input("Ingrese la ciudad de origen del huesped: ")
                   #NUMERO DE DIAS
                   D=int(input("Ingrese el número de Días: "))
                   #TOTAL A PAGAR
                   T=num_pers*h3*D
                   #FORMA DE PAGO
                   fpago=input("Ingrese la forma de pago: ")

                   #SE AGREGAN A LAS LISTAS
                   fP.append(fpago)
                   Tp.append(T)
                   nD.append(D)
                   nH.append(h)
                   Name.append(n)
                   cdOr.append(cor)
                   NumP.append(num_pers)
        #BUSQUEDA
        case 2:
            print("===BUSQUEDA===")
            if os.path.exists("reporte.txt"):
                hab=(input("¿Que habitacion o huesped desea buscar? ")) 
                archivo=open("reporte.txt", "r")
                encontrado=False    
                for linea in archivo:
                    if hab in linea:
                        print("ENCONTRADO: ", linea.strip())
                        encontrado=True
                if not encontrado:
                        print("NO ENCONTRADO")
                archivo.close()
        #REPORTE
        case 3:
            print("===REPORTE===")
            print("Eliga una opcion")
            opc=input("Eliga una opción:\na)Mostrar toda la información (archivo)\nb)Tabla de habitaciones ocupadas y libres\n")
            match opc:
                case 'a':
                    nombre_archivo = "reporte.txt"
                    with open(nombre_archivo, "w") as file:
                        file.write("REPORTE DE HABITACIONES OCUPADAS\n")
                        file.write("=" * 90 + "\n")
                        # Encabezados con el formato de tu imagen
                        file.write(f"{'CUARTO':<10}{'NOMBRE':<15}{'CIUDAD':<15}{'DIAS':<10}{'PERSONAS':<15}{'TOTAL':<10}{'PAGO':<10}\n")
                        file.write("-" * 90 + "\n")
                        for i in range(len(nH)):
                            linea = f"{nH[i]:<10}{Name[i]:<15}{cdOr[i]:<15}{nD[i]:<10}{NumP[i]:<15}{Tp[i]:<10}{fP[i]:<10}\n"
                            file.write(linea)
                    
                    print(f"\n--> Archivo '{nombre_archivo}' generado exitosamente.")

                case 'b':
                    print(f"\n{'CUARTO':<10}{'NOMBRE':<15}{'TOTAL':<10}")
                    print("-" * 35)
                    for i in range(len(nH)):
                        print(f"{nH[i]:<10}{Name[i]:<15}{Tp[i]:<10}")
        case 4:
            print("=== MODIFICACIONES ===")
            mod = int(input("Habitación a modificar: "))
            
            if mod in nH:
                idx = nH.index(mod)
                print(f"Días actuales: {nD[idx]}")
                nuevos_dias = int(input("Nuevos días: "))
                
                costo_unitario = Tp[idx] / nD[idx]
                nuevo_total = int(nuevos_dias * costo_unitario)
                
                nD[idx] = nuevos_dias
                Tp[idx] = nuevo_total
                print(f"--> Actualizado. Nuevo total: ${nuevo_total}")
                print("NOTA: Vuelve a generar el reporte (Opción 3a) para actualizar el archivo.")
            else:
                print("Habitación no encontrada.")
        #ELIMINAR
        case 5:
            print("=== ELIMINAR ===")
            # SIN TRY
            eli = int(input("Habitación a eliminar: "))
            
            if eli in nH:
                idx = nH.index(eli)
                nH.pop(idx)
                Name.pop(idx)
                nD.pop(idx)
                cdOr.pop(idx)
                Tp.pop(idx)
                fP.pop(idx)
                NumP.pop(idx)
                print(f"--> Habitación {eli} eliminada.")
                print("NOTA: Vuelve a generar el reporte (Opción 3a) para actualizar el archivo.")
            else:
                print("Habitación no encontrada.")
        #SALIDA
        case 6:
            print(f"Ingresos totales del día: ${sum(Tp)}")
            break
print("Ha salido del programa")