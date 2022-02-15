from re import L
import time
from Menu import Menu
from Dim import gotoxy, cls, ValidarNum, msg
from Lista import Lista
from Pilas import Stack
from Colas import Queue

MenuObj = Menu()
DatLisObj = Lista()
DatPilObj = Stack()
DatColObj = Queue()
ListPrin = ["Lista","Pilas","Colas","Salir"]
ListSub = ["Push","Pop","Show","Eliminar","Insertar","Buscar","Volver"]
ListSub1 = ["Cambiar Tamaño de lista","Push","Pop","Show","Buscar","Longitud","Volver"]
cls()
Opc = ""

while Opc != "4":
    Opc = MenuObj.menu(ListPrin,"Menú")
    SubOpc = ""
    if Opc == "1":
        cls()
        while SubOpc != "7":
            SubOpc = MenuObj.menu(ListSub,"Menú - Listas")
            cls()
            if SubOpc == "1":
                gotoxy(1,1);Dato = ValidarNum(19,1,"Ingrese el valor: ")
                DatLisObj.insertar(Dato)
                gotoxy(len(str(Dato))+20,1);print("¡Dato ingresado!");time.sleep(1)
                cls()
            elif SubOpc == "2":
                print(DatLisObj.obtener())
                msg(1)
            elif SubOpc == "3":
                DatLisObj.mostrar()
                msg(1)
            elif SubOpc == "4":
                Pos = ValidarNum(30,1,"Ingrese posición a eliminar: ")
                PosBool = DatLisObj.eliminarElemento(Pos)
                gotoxy(1,2);print(PosBool if PosBool else "posicion: {} no valida".format(Pos))
                msg(1)
            elif SubOpc == "5":
                gotoxy(1,1);Dato = ValidarNum(30,1,"Ingrese el valor a insertar: ")
                Pos = ValidarNum(40,2,"Ingrese posición del valor a insertar: ")
                DatLisObj.insertarElemento(Pos,Dato,40,2)
                msg(1)
            elif SubOpc == "6":
                OpcBusc = 0
                if DatLisObj.empty():
                    print("Lista vacía, nada que buscar.")
                    msg(1)
                else:
                    gotoxy(1,1);print("Presione 1 para buscar por valor o 2 para buscar por posición.")
                    while True:
                        try:
                            OpcBusc = ValidarNum(1,2,"")
                            if OpcBusc > 0 and OpcBusc <= 2:
                                break
                        except:
                            gotoxy(1,2);msg(2)
                            time.sleep(1)
                            gotoxy(1,2);print(" "*5)
                        else:
                            gotoxy(1,2);print("Ingrese 1 o 2")
                            time.sleep(1)
                            gotoxy(1,2);print(" "*30)
                    cls()
                    DatLisObj.Buscar(OpcBusc, "La posición de su valor", "El valor de la posición")
    elif Opc == "2":
        cls()
        while SubOpc != "7":
            if DatPilObj.tamanio():
                DatPilObj = Stack(ValidarNum(28,1,"Ingrese tamaño de la pila: "))
                cls()
            SubOpc = MenuObj.menu(ListSub1,"Menú - Pilas")
            cls() #* ["Cambiar Tamaño de Pila","Push","Pop","Show","Buscar","Longitud","Volver"]
            if SubOpc == "1":
                DatPilObj = Stack(ValidarNum(37,1,"Ingrese el tamaño de la nueva pila: "))
                cls()
            elif SubOpc == "2":
                gotoxy(1,1);Dato = ValidarNum(18,1,"Ingrese el dato: ")
                if DatPilObj.full():
                    DatPilObj.push(Dato)
                    gotoxy(len(str(Dato))+20,1);print("¡Dato ingresado!");time.sleep(1)
                else:
                    print("La Pila está Llena")
                    msg(1)
                cls()
            elif SubOpc == "3":
                print(DatPilObj.pop())
                msg(1)
            elif SubOpc == "4":
                DatPilObj.show()
                msg(1)
            elif SubOpc == "5":
                DatPilObj.buscar(ValidarNum(28,1,"Ingrese su valor a buscar: "))
                msg(1)
            elif SubOpc == "6":
                print("El tope de la lista es {}".format(DatPilObj.longitud()))
                msg(1)
    elif Opc == "3":
        cls()
        while SubOpc != "7":
            if DatColObj.tamanio():
                DatColObj = Queue(ValidarNum(28,1,"Ingrese tamaño de la cola: "))
                cls()
            SubOpc = MenuObj.menu(ListSub1,"Menú - Colas")
            cls() #* ["Cambiar Tamaño de Cola","Push","Pop","Show","Buscar","Longitud","Volver"]
            if SubOpc == "1":
                DatColObj = Queue(ValidarNum(37,1,"Ingrese el tamaño de la nueva cola: "))
                cls()
            elif SubOpc == "2":
                gotoxy(1,1);Dato = ValidarNum(18,1,"Ingrese el dato: ")
                if DatColObj.full():
                    DatColObj.push(Dato)
                    gotoxy(len(str(Dato))+20,1);print("¡Dato ingresado!");time.sleep(1)
                else:
                    print("La Cola está Llena")
                    msg(1)
                cls()
            elif SubOpc == "3":
                print(DatColObj.pop())
                msg(1)
            elif SubOpc == "4":
                DatColObj.show()
                msg(1)
            elif SubOpc == "5":
                DatColObj.buscar(ValidarNum(28,1,"Ingrese su valor a buscar: "))
                msg(1)
            elif SubOpc == "6":
                print("El tope de la lista es {}".format(DatColObj.longitud()))
                msg(1)
    elif Opc == "4":
        cls()
        print("Usted está saliendo...");time.sleep(1)
    elif Opc not in range(0,len(ListPrin)):
        gotoxy(30,7);print("Ingrese un número válido!")
        time.sleep(1)
        gotoxy(30,7);print(" "*27)