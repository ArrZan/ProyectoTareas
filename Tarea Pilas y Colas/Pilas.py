class Stack:                
    def __init__(self,tamanio=0):
        self.lista=[]
        self.tope=0
        self.size=tamanio

    def empty(self):
        return self.tope == 0

    def tamanio(self):
        return self.size == 0

    def full(self):
        return len(self.lista) != self.size

    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1

    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top

    def longitud(self):
        return self.tope

    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))

    def buscar(self,buscado):
        if buscado in self.lista:
            for pos in range(self.tope-1,-1,-1):
                if buscado == self.lista[pos]:
                    print("La posición es {}".format(pos+1))
        else:
            print("-1")
