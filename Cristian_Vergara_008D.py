import csv
import time
import os
import random

LimpiarCMD = "cls"
    
try:
    with open("Pedido_Comida.csv", "x") as pedido_comida:
        escritor_csv = csv.writer(pedido_comida)
except FileExistsError:
    pass


with open("Pedido_Comida.csv", "w", newline="") as pedido_comida:
    escritor_csv = csv.writer(pedido_comida)
    escritor_csv.writerow(["Num. Pedido", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"])

    
with open("Pedido_Comida.csv", "r", newline="") as pedido_comida:
    lector_csv = csv.reader(pedido_comida)
    for fila in lector_csv:
        print(fila)

with open("Pedido_Comida.csv", "r") as pedido_comida:
    lector_csv = csv.reader(pedido_comida)
    encabezado = next(lector_csv, 0)
    if encabezado != ["Num. Pedido", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]:
        with open("Pedido_Comida.csv", "a") as pedido_comida:
            escritor_csv = csv.writer(pedido_comida)
            escritor_csv.writerow(["Num. Pedido", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"])

with open("Pedido_Comida.csv", "r", newline="") as pedido_comida:
    lector_csv = csv.reader(pedido_comida)
    for fila in lector_csv:
        print(fila[0])

os.system(LimpiarCMD)

def menu():
    print(" "*10, "MENU")
    print("Seleccione una de las siguientes opciones: \n")
    print("1. Registrar Pedido.")
    print("2. Listar todos los pedidos.")
    print("3. Imprimir hoja de ruta.")
    print("4. Salir")

    
def RegPedido():
    NumPedido = random.randint(1,1000)
    NumPedido = ""
    NomPedido = ""
    DirPedido = ""
    LugPedido = ""
    Sac5kg = 0
    Sac10kg = 0
    Sac20kg = 0

    NomPedido = input("Ingrese su nombre y apellido: \n")
    if len(NomPedido) <= 3:
        print("Ingrese un nombre correcto.")
    else:
        print("Usuario ingresado correctamente.")
        time.sleep(1)
        os.system(LimpiarCMD)

    DirPedido = input("Ingrese su dirreción \n")
    if len(DirPedido) <= 3:
        print("Ingrese una dirección correcta.")
    else:
        print("Dirección añadida correctamente al pedido.")
        time.sleep(1)
        os.system(LimpiarCMD)

    print("Seleccione una de las siguientes comunas: \n1. San Bernardo \n2. Calera de Tango \n3. Buin")
    LugPedido = int(input(""))
    if LugPedido == 1:
        print("Sector agregado correctamente.")
        LugPedido = "San Bernardo"
        time.sleep(1)
        os.system(LimpiarCMD)
    elif LugPedido == 2:
        print("Sector agregado correctamente.")
        LugPedido = "Calera de Tango"
        time.sleep(1)
        os.system(LimpiarCMD)
    elif LugPedido == 3:
        print("Sector agregado correctamente.")
        LugPedido = "Buin"
        time.sleep(1)
        os.system(LimpiarCMD)
    else:
        print("Ingrese una opción correcta, entre 1 y 3")
    
    Sac5kg = int(input("¿Cuantos sacos de 5 kilos desea comprar? \n"))
    if Sac5kg >= 0:
        print("Cantidad agregada correctamente.")
    else:
        print("Ingrese una cantidad correcta.")
    
    Sac10kg = int(input("¿Cuantos sacos de 10 kilos desea comprar?\n"))
    if Sac10kg >= 0:
        print("Cantidad agregada correctamente.")
    else:
        print("Ingrese una cantidad correcta.")
    
    Sac20kg = int(input("¿Cuantos sacos de 20 kilos desea comprar?\n"))
    if Sac20kg >= 0:
        print("Cantidad agregada correctamente.")
    else:
        print("Ingrese una cantidad correcta.")
    
    with open("Pedido_Comida.csv", "a", newline="") as pedido_comida:
        escritor_csv = csv.writer(pedido_comida)
        escritor_csv.writerows([
            [NumPedido, NomPedido, DirPedido, LugPedido, Sac5kg, Sac10kg, Sac20kg]
        ])
    
    OtrPedido = int(input("¿Desea realizar otro pedido?\n1. Si \n2. No \n"))
    if OtrPedido == 1:
        NumPedido += 1
        time.sleep(1)
        os.system(LimpiarCMD)
        RegPedido()
    elif OtrPedido == 2:
        time.sleep(1)
        os.system(LimpiarCMD)
        menu()
    else:
        print("Ingrese un valor valido, entre 1 y 2.")

    
MenuEntero = 1

while MenuEntero == 1:
    menu()
    opcMenu = int(input(""))
    if opcMenu == 1:
        RegPedido()

    elif opcMenu == 2:
        with open("Pedido_Comida.csv", "r", newline="") as pedido_comida:
            lector_csv = csv.reader(pedido_comida)
            for i in lector_csv:
                if i:
                    print(", ".join(i))
    
    elif opcMenu == 3:
        with open("Pedido_Comida.csv", "r", newline="") as pedido_comida:
            lector_csv = csv.reader(pedido_comida)
            for fila in lector_csv:
                print([0, 1, 2, 3])

    elif opcMenu == 4:
        MenuEntero += 1
        print("Saliendo del programa, muchas gracias.")

    else:
        print("Ingrese una opción correcta.")