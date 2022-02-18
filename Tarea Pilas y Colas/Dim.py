import os, time

def cls():
    os.system("cls")

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def msg(ind):
    if ind == 3:
        print("Ingrese sólo caracteres...")
    if ind == 2:
        print("Ingrese un dato válido")
    elif ind == 1:
        input("\nPresione una tecla para salir...")
        cls()
    elif ind == 0:
        print("Ingrese sólo valores numéricos...")

def ValidarNum(col,fil,inf):
        print(inf)
        while True:
            gotoxy(col,fil);valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);msg(0)
                time.sleep(1)
                gotoxy(col,fil);print(" "*33)
        return int(valor)