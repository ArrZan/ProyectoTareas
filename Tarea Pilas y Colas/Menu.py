from Dim import gotoxy

class Menu:
    def __init__(self,col=1,fil=1):
        self.col=col
        self.fil=fil

    def menu(self,opciones,titulo):
        self.col=1
        self.fil=1
        gotoxy(self.col,self.fil);print("*"*20,titulo,"*"*20)
        ct=0
        for opcion in opciones:
            ct+=1
            self.fil +=1
            gotoxy(self.col,self.fil);print("{}) ".format(ct),opcion)
        gotoxy(self.col,self.fil+2)
        opc = input("Escoja una Opcion[1...{}]: ".format(len(opciones)))
        return opc