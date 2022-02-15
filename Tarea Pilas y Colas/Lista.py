from Dim import gotoxy, ValidarNum, msg
import time

class Lista:
    def __init__(self,datos=[]) -> None:
        self.lista=datos
    
    def empty(self):
        return len(self.lista) == 0
    
    def insertar(self,dato):
        self.lista.append(dato)
        
    def obtener(self):
        if self.empty():
            print("Lista vacia")
        else:
            return self.lista.pop()

    def eliminarElemento(self,pos):
        pos = pos-1
        if pos in range(0,len(self.lista)):
                ele = self.lista[pos]
                self.lista = self.lista[0:pos] + self.lista[pos+1:]
                return ele
        else:
                return None

    def insertarElemento(self,pos,dato,col,fil):
        pos-=1
        if not self.empty():
            while pos not in range(0,len(self.lista)):
                gotoxy(col,fil);print("Posición inválida")
                time.sleep(1)
                gotoxy(col,fil);print(" "*50);
                gotoxy(col,fil);pos = ValidarNum(col,fil,"")
                pos-=1
        else:
            print("Lista vacía")

        if pos in range(0,len(self.lista)):
            ele = self.lista[pos]
            self.lista = self.lista[0:pos] + [dato] + self.lista[pos:]
            print(self.lista)
        
    def mostrar(self):
        if len(self.lista) == 0:
            print("Lista vacia")
        else:
            print("Datos de lista")
            for i in self.lista:
                print(i)
    
    def Buscar(self, Opcion, inf1, inf2):
        if Opcion == 1:
            valor = ValidarNum(28, 1, "Ingrese su valor a buscar: ")
            for pos in range(0,len(self.lista)):
                if valor == self.lista[pos]:
                    print("{} {} es {}".format(inf1, valor, pos+1))    
            msg(1)
        elif Opcion == 2:
            pos = ValidarNum(31,1,"Ingrese su posición a buscar: ")
            for i in range(0,len(self.lista)):
                if pos-1 == i:
                    print("{} {} es {}".format(inf2, pos, self.lista[pos-1]))    
            msg(1)