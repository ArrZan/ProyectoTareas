
from math import factorial
import re

class ejerciciosTAREA2:
    
    def ejerVIDEO1_1(self):
        # ¿Podrias decir que guarda la variable (X)?
        X=46
        X=15
        x=30
        print("X = 46\nX = 15\nx = 30\nX =",X)
        X=10*2
        X-=5    
        print("\nX = 10*2\nX -= 5\nX =",X)
        X=10-2
        10+2
        print("\nX = 10-2\nX = 10+2\nX =",X)
        Y=3*(4+2)
        X=Y+2
        Z=5
        X=Y-Z
        print("\nY = 3*(4+2)\nX = Y+2\nZ = 5\nX = Y-Z\nX =",X)
        X=25
        X+10
        print("\nX = 25\nX=+10\nX =",X)
        X=3
        Y=X+6
        X=Y-1
        print("\nX = 3\nY = X+6\nX = Y-1\nX =",X)

    def ejerVIDEO2_1(self):
        # ¿ De que tipo es cada uno de estos datos?
        a=100/5
        tipoDATO=type(a)
        print("A.) 100/5 es tipo..  ",tipoDATO)
        b=7/2
        tipoDATO=type(b)
        print("B.) 7/2 es tipo..    ",tipoDATO)
        c=7//2
        tipoDATO=type(c)    
        print("C.) 7//2 es tipo..   ",tipoDATO)
        d=7%2
        tipoDATO=type(d)
        print("D.) 7%2 es tipo..    ",tipoDATO)
        e='a'
        tipoDATO=type(e)    
        print("E.) 'a' es tipo..    ",tipoDATO)
        f="tiza"+"."
        tipoDATO=type(f)
        print("E:) tiza""+""." "es tipo..   ",tipoDATO)
        g="hola"[1+1]
        tipoDATO=type(g)
        print("F.) hola""[1+1]""es tipo..   " ,tipoDATO) 
        h=len("hola")
        tipoDATO=type(h)
        print("G.) len(""hola"") es tipo..  ",tipoDATO)
        i=int("145")
        tipoDATO=type(i)
        print("H.) int(""145"") es tipo..   ",tipoDATO) 
        j=float("145")
        tipoDATO=type(j)
        print("I.) float(""145"") es tipo..     ",tipoDATO) 
        k=float(145)
        tipoDATO=type(k)
        print("J.) float(145) es tipo..     ",tipoDATO) 
        l=str(32)
        tipoDATO=type(l)
        print("K.) str(32) es tipo..    ",tipoDATO) 
        m=1+2!=3
        tipoDATO=type(m)
        print("L.) 1+2!=3 es tipo..     ",tipoDATO) 
        n=177%2==0
        tipoDATO=type(n)
        print("N.) 177%2==0 es tipo..   ",tipoDATO) 
        ñ=len("nube")<=20
        tipoDATO=type(ñ)
        print("M.) len(""nube"")<=20 es tipo..  ",tipoDATO) 


    def ejerVIDEO2_2_1():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=a=11-(4%2+10)
        print(a)
    def ejerVIDEO2_2_2():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="tiza"+"."
        print(a)
    def ejerVIDEO2_2_3():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="30"+2
        print(a)  
    def ejerVIDEO2_2_4():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="hola"+[len("hola")]
        print(a)
    def ejerVIDEO2_2_5():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=len(142)
        print(a)
    def ejerVIDEO2_2_6():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="hola"[len("fin")]
        print(a)
    def ejerVIDEO2_2_7():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="hola"[11-(4%2+10)]
        print(a)
    def ejerVIDEO2_2_8():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=int("4")
        print(a)
    def ejerVIDEO2_2_9():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=int(4)
        print(a)
    def ejerVIDEO2_2_10():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=int("z")
        print(a)
    def ejerVIDEO2_2_11():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=int("4.")
        print(a)
    def ejerVIDEO2_2_12():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a=4<"f"
        print(a)
    # def ejerVIDEO3_2_13():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        # a="palabra"="rama"
        # print(a)
    def ejerVIDEO2_2_14():
        # ¿ CAUL DE LAS SIGUIENTES OPERACIONES DA ERROR?
        a="palabra"=="rama"
        print(a)

    def ejerVIDEO3_1():
        a=not True
        b=not(1+2!=3)
        x=(len("jugar")>5) and (len("jugar")<10)
        c="alto"[2]=="t" and x
        d=842913%10!=3 and len("cafe")==3
        e=0!=0 or "a"<"y"
        f=True or int("50")>=50
        edad=20
        not(x) or edad%2==0
        es_cliente=False
        not(es_cliente and not (edad<18))

        print("A.) not True:    Es",a)
        print("B.) not(1+2!=3):  Es",b)
        print("C.) (len(""jugar"")>5) and (len(""jugar"")<10):   Es",x)
        print("D.) alto""[2]""==""t"" and x:     Es",c)
        print("E.) 842913%10!=3 and len(""cafe"")==3:      Es",d)
        print("F.) 0!=0 or ""a""<""y:"      "Es""",e)
        print("G.) True or int(""50"")>=50:      Es",f)
    
    def ejerVIDEO3_2():
        # Que errores tienen estas proposiciones? ¿Como deben corregirse?
        #? El numero no puede ser menor que 0 ni mayor que 100
        #? numero<0 and numero >100
        numero=int(input("ingresar numero entre 0-100: "))
        if numero<0 and numero >100:
            print(numero)
        else:
            print("error")

        #* correción
        if numero>=0 and numero<=100:
            print(numero)
        else:
            print("error")

        #? Edad debe estar entre 10 y 20
        #? edad>10 and <20
        edad=int(input("ingresar edad entre 10-20: "))
        # if edad>10 and <20:
        #     print(numero)
        # else:
        #     print("error")

        #* correción
        if edad>10 and edad<20:
            print(numero)
        else:
            print("error")

        #?La longuitud de la cadena no debe ser superior a 10 caracteres 
        cadena=str(input("ingresar cadena de caracteres:"))
        caracteres=len(cadena)<=10
        print(caracteres)

    def ejerVIDEO3_3():
        # ¿Cómo expresarías las siguientes operaciones?
        #! ejercicio 1
        #? El numero es multiplo 4 y tambien es negativo.
        numero=int(input("ingrese un numero: "))
        if numero%4==0 and numero<0:
            print("correcto")
        else:
            print("error")
        #! ejercicio 2
        #? Decidiste comprar un auto usdo, pero debe cumplir ciertas condiciones:
        #? El kilometraje debe se menor a 3000 y el modelo debe estar entre 2015 y2017 
        km=int(input("Ingrese el kilometraje del auto: "))
        modelo=int(input("Ingrese el año del modelo del Carro: "))
        if km<3000 and (modelo>=2015 and modelo<=2017):
            print("Lo compro")
        else:
            print("No lo compro")   
        #! ejercicio 3
        #? Una agrupacion academica tiene ciertos requesitos para caulquier estudiante
        #? que desea ingresar: debe tener mas del 30% de sus estudios completos y no debe ser miembro 
        #? de otra agrupacion academica en la misma universidad.
        porcentaje=int(input("Ingrese el porsentaje de sus estudios(%): "))
        agrupacion=str(input("¿Pertenece a alguna agrupacion?. ingrese (si) o (no) :"))
        if porcentaje>30:
            if agrupacion=="no":
                print("Si puede ingresa ")
            else:
                print("No puede ingresar ")
        else:
            print("No puede ingresar ")
            
        #! ejercicio 4
        #? Una persona pasa frio si es invierno y ademas no tiene calefacion ni esta abrigada.
        invierno=str(input("¿Es invierno? ingrese (si) o (no) :"))
        negacion=not(invierno)
        print(negacion)

    def ejerVIDEO4_1():
        cadena="sí, profe, es cierto... yo me comi la tarea"
        #? ¿Cual es el resultado?
        cadena[10]
        cadena[-1]
        cadena[0:9]
        cadena[::3]
        # respuesta 
        print ("'",cadena[10],"'")
        print ("'",cadena[-1],"'")
        print ("'",cadena[0:9],"'")
        print ("'",cadena[::3],"'")
        #? ¿como obtener?
        #! La cadena al revés: "aerat al imoc em oy ...otresic se ,eforp ,ís"
        # respuesta
        print("'",cadena[::-1],"'")
        #! la subcadena "profe"
        # respuesta
        print("'",cadena[4:9],"'")

    def ejerVIDEO4_2():
        #? Dada la variable s="   hola, ¿cómo estás?" con 3 espacios al inicio,
        #? ¿que se obtine en cada una de kas suguientes operaciones?
        s="   hola, ¿cómo estás?"
        print("'",s[::-1],"'")
        # print("'",s[len(s)],"'") #! <= provoca error 
        print("'",s.count("o"),"'")
        print("'",s.count("Hola"),"'")
        print("'",s[-4:],"'")
        print("'",s[15:],"'")
        print("'",s.find("o"),"'")
        print("'",s.strip(),"'")
        #print("'",x=s.upper())
        #print("'",x==s,"'")
        print("'",s[14:].upper(),"'")
        print("'",len(s)%2!=0,"'")
        print("'",s.replace(" ", "*"),"'")
        print("'",s.replace("z", "Z"),"'")

    def ejerVIDEO4_3():  
        #? Dada la variable X de tipo string ¿como se pude hallar el indice
        #? del ultima caracter?
        x="Brigner Ariel Carriel Rodriguez"
        print(x[-1])
        #? Dada la variable cadena="hola" ¿que retorna cadena.find("2")?
        cadena="hola"
        print(cadena.find("2"))
        #? ¿Que retorna? "a" in "dátiles"
        print("a"in"dátiles")
        #? ¿Que operacion retorna la posicion del primer espacio en "me gusta programar"
        cade="me gusta programar"
        print(cade.find(" "))
        #? ¿Que operacion retorna la cantidad de espacios de la cadena "me gusta programar"?
        cad="me gusta programar"
        print(cad.count(" "))
        #? ¿Por que da error? cadena[0]="H"

        #? ¿Que almacena la siguiente varible? nueva="c"+cadena[1:]
        nueva="c"+cadena[1:]
        print(nueva)
        #? ¿como remplazar las vocales acentuadas por vocales no acentuadas en la cadena X?
        x="hoy es día miércoles"
        print(x.replace("í","i".replace("é","e")))
        #? ¿que comparacion podria hacerse para averiguar si la longuitud de la cadena es par?
        x="hoy es día miércoles"
        longuitud=len(x)
        if len(x)//2:
            print("La longuitud es par ",longuitud)
        else:
            print("La longuitud es impar ",longuitud) 
        #? ¿De que forma se puede obtener la cantiad de vocales de la cadena X?  
        x="hoy es dia miercoles"
        a=x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u")
        print(a)
    def ejerVIDEO5_1():
        #! ¿que problemas tienen las siguientes intrucciones?¿ como los sulucionarias?
        # ? A=input(nombre,"¿cual es tu cancion favorita?")
        print('print(nombre,"¿cual es tu edad?")')
        A=input()
        # ? precio=input("Precio:")
        # ? total=precio+(precio*0.10)   
        print("**Siguiente Ejercicio**")
        precio=float(input("Precio:"))
        total=precio+(precio*0.10)
        #? edad=int(input("Edad:"))
        #? print(tu edad es, edad)
        print("**Siguiente Ejercicio**")
        edad=int(input("Edad:"))
        print("tu edad es", edad)
        #? edad=int(input("edad:"))
        #? print("veamos si tu edad es 18..", edad=0)    
        print("**Siguiente Ejercicio**")
        edad=int(input("edad:"))  
        print("veamos si tu edad es 18..",edad==0)  

    def ejerVIDEO5_2():
        #? Solicito al usuario que ingrese su nombre. el nombre se debe almacenar en una variable llamado N.
        #? A continuacion se debe mostrar en la pantalla el texto "Ahora estas en la matrix, [usuario]" se
        #? se reemplazara por el nombre que el usuiario haya ingresado
        texto="Ahora estas en la matrix, [usuario]"
        print(texto)
        N=input("ingrese nombre: ")
        reemplaso=texto.replace("usuario",N)
        print(reemplaso)

    def ejerVIDEO5_3():
        #? Hacer un progrma que solicite al usuario cuánto costó una cena en en un restaurante. A ese valor,
        #? sumarle un 6.2% en concepto de servicio y un 10% de propina.
        #? Inprimir en pantalla el nonto final a pagar.
        valor=float(input("Cuanto costo la cena en el restaurante: $"))
        servicio=valor*0.062
        propina=valor*0.1
        valor_pagar=valor+servicio+propina
        valor_pagar1=round(valor_pagar,2)
        print("valor total a pagar es: $",valor_pagar1)
    def ejerVIDEO5_4(): 
        #? Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en un a variable numerica(en total, tres variables diferentes).finalmente, mostrar la fecha en formato dd/mm/aaa.
        dia=int(input("ingrese el dia: "))
        mes=int(input("ingrese el mes: "))
        año=int(input("ingrese el año: "))
        print(dia,"/",mes,"/",año)
        #? Hacer otra vercion del programa, pero esta vez almacenando todo en una variable numerica, en la forma DDMMAAAA ¿y si la varible fuera de tipo string?  
        print("**Siguiente Ejercicio**")
        dia=input("ingrese el dia: ")
        mes=input("ingrese el mes: ")
        año=input("ingrese el año: ")
        fecha=dia+"/"+mes+"/"+año
        print(fecha)
        #! ¿y si la varible fuera de tipo string? 
        fecha=input("Ingrese la fecha en formato DDMMAAAA: ")
        dia=fecha[:2]
        mes=fecha[2:4]
        año=fecha[4:] 
        print(dia,"/",mes,"/",año) 
    def ejerVIDEO5_5():
        #? Una pareja de motociclistas necesitas hacer ciertos calculos antes de emprender un viaje en moto, para saber cuanntos tanques de combustible consumira el viaje ebtero
        #* para eso deben ingresar: cuantos kilometros puede recorrer su moto con un 1 litro de combustible, que capacidad(en litros)tiene el tanque y cuantos kilometros en total recorreran
        #! hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de conbustible necesarios.
        capacidad=float(input("Capaciad del tanque: "))
        kmxl=float(input("Rendimiento(km por litro): "))
        recorrido=float(input("Km totales a recorrer: "))
        kmxlcapacidad=capacidad*kmxl
        print("Son necesarios", recorrido/kmxlcapacidad,"litros.")
    def ejerVIDEO6_1():
        #? Escribir un programa que, dado un número entero, muestre su valor absoluto.
        #? Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos,
        #?  su valor absoluto es el número multiplicado por men -1(valor absoluto de -52 es 52).
        numero=int(input("Ingrse el numero: "))
        if numero<0:
            numero=numero*-1
        print("El valor absoluto es",numero)
        #? Solicitar al usuario que ingrese los nombres de dos personas los cuales se almacenarán en dos
        #? variables. A continuación, imprimir "coincidencia" si los nombres de ambas personas comienzan con la misma letra o si terminan 
        #? con la misma letra. Si no es así, imprimir "no hay coincidencia".
        print("**Siguiente Ejercicio**")
        primerNOMBRE=input("primer nombre: ")
        segundoNOMBRE=input("segundo nombre: ")
        if primerNOMBRE[0]==segundoNOMBRE[0] or primerNOMBRE[-1]==segundoNOMBRE[-1]:
            print("Coincidencia")
        else:
            print("No hay Coincidencia")
        #? Crear un programa que permite al usuario elegir un candidato por el cual votar. Las posibilidades son: candidatos A por el partido rojo, 
        #? candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B o C) se le debe imprimir el mensaje "usted 
        #? ha votado por el partido [color que corresponde al candidato elegido]". Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles indicar opción errónea.
        print("**Siguiente Ejercicio**")
        Candidato=input("Elegir candidato(A,B,C): ")
        if Candidato.upper()=="A":
            print("Usted ha botado por el rojo")
        elif Candidato.upper()=="B":
            print("Usted ha botado por el azul")
        elif Candidato.upper()=="C":
            print("Usted ha botado por el verde")
        else:
            print("Opcion erronea")
        #? Escribir un programa que solicité al usuario una letra y, si es una vocal, muestre el mensaje "es vocal". 
        #? se debe validar que el usuario ingrese solo un carácter ingresa un string demás de un carácter, informarle que no se puede procesar el dato.
        print("**Siguiente Ejercicio**")
        letra= input("ingrese una letra: ")
        if len(letra)!=1:
            print("Debe ser solo una letra")
        else:
            if letra.lower() in "aeiou":
                print("es una vocal")
            else:
                print("no es una vocal")
        #? Hacer un programa qur prtmita saber si un año es bisiesto,
        #? para que una año sea bisiesto debe ser dibisible por 4 u no debe ser divisible por 100,
        #? excepto que tambien sea divisible por 400.
        print("**Siguiente Ejercicio**")
        año=int(input("Año: "))
        if año%4!=0:
            print("No es bisiesto")
        else:
            if año%100!=0 or año%400==0:
                print("Es bisiesto")
            else:
                print("No es bisiesto")
    def ejerVIDEO7_1():            
        #? Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
        #? ¿Qué modificación habría que hacer si ahora solo se deben sumar los números que sean múltiplos de 3?
        total=0
        for i in range(101):
            if i%3==0:
                total+=i
        print("sumatoria:", total)
        #? Dado un número entero positivo mostrar su factorial.
        #? El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
        #? El factorial de 0 es 1.
        print("**Siguiente Ejercicio**")
        numero=0
        while numero<=0 or numero>=100 :
            numero=int(input("Numero: "))
        f=1
        if numero!=0:
            for i in range(1,numero+1):
                f=f*i
        print("factorial:",f)
        #? Crear un algoritmo que muestre los primeros 10 números de la sucesión de fibonacci la sucesión comienza con los números
        #?  0 y 1 y a partir de estos cada elemento es la suma de los dos números anteriores en la secuencia.
        print("**Siguiente Ejercicio**")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range (8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
        #? Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos.
        #? No olvides que no es posible dividir por cero por lo que es necesario evitar que el programa arroje un error sino se ingresaron números positivos.
        print("**Siguiente Ejercicio**")
        sumaNegativo=0
        sumaPositivo=0
        cantidadPositivo=0
        for i in range(6):
            nro=int(input("numero: "))
            if nro>=0:
                cantidadPositivo+=1
                sumaPositivo+=nro
            else:
                sumaNegativo+=nro
        print("Sumatoria de negativos:",sumaNegativo)
        if cantidadPositivo!=0:
            print("promedio de positivo:", sumaPositivo/cantidadPositivo)
        else:
            print("no se ingresan numeros positivos")
    def ejerVIDEO7_2():

        corrimiento=int(input("corrimiento: "))
        alfabeto="abcdefghijklmnñopqrstuvwxyz"

        for i in range(5):
            mensaje=input("mensaje a escriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower()in alfabeto:
                    indice=alfabeto.find(caracter.lower())
                    indice=(indice+corrimiento)%27
                    encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
            print("***mesaje encriptado:",encriptado)
    def ejerVIDEO8_1():      
        total=0
        monto=float(input("Monto de una venta: $"))
        while monto!=0:
            if monto<0:
                print("Monto no valido")
            else:
                total+=monto
            monto=float(input("Monto de una venta: $ "))
        if total>1000:
            total-=total*0.1
        print("Monto total a pagar: $", total)


        totalpares=0
        totalimpares=0
        numero=int(input("Numero: "))
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:
                ultimaDigito=numero%10
                if ultimaDigito%2==0:
                    pares+=1
                    totalpares+=1
                else:
                    impares+=1
                    totalimpares+=1
                numero=numero//10
            print("El numero ingresado tiene",pares,"dijitos pares y", impares,"dijitos impares")
            numero=int(input("Numero: ")) 
        print("Total de dijitos pares:",totalpares)
        print("Total de dijitos impares:",totalimpares)

        digitosEnlalinea=0
        cantidadlinea=0
        titulo=input("Titulo del libro: ")
        while titulo!="'":
            if titulo!="/":
                cantidadlinea+=1
                print("linea completa. aparecen", digitosEnlalinea,"digitos")
                digitosEnlalinea=0
            else:
                for caracter in titulo:
                    if caracter in "0123456789":
                        digitosEnlalinea+=1
            titulo=input("titulo del libro: ")
        print("FIN. se leyeron", cantidadlinea,"lineas")

    def ejerVIDEO9_1():
        cantidad=0
        n=int(input("Numero: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                    primo=False
                    break
            if primo:
                cantidad+=1
            n=int(input("Numero: "))
        print("primos",cantidad)

        añoinicio=int(input("Año incial: "))
        añofin=int(input("Año final: "))
        for año in range(añoinicio,añofin+1):
            if not año%10==0:
                continue
            if not año%4==0:
                continue
            if año%100!=0 or año%400!=0:
                print(año)

    def ejerVIDEO10_1(self):
        def validar(email):
            caracterbuscado="@"
            emailvalido=False
            for c in email:
                if c==caracterbuscado:
                    emailvalido=True
                    break
            return emailvalido

        direccion=input("tu email: ")
        if validar(direccion):
            print("direccion valida")
        else:
            print("direccion invalida")

    def ejerVIDEO10_1_2(self):
        def sumadigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma
        #! programa principal
        num=int(input("Numero a procesar: "))
        while num!=0:
            print("Suma:", sumadigitos(num))
            num=int(input("numero a procesar: "))     

    def ejerVIDEO10_1_3(self):
        def sumadigitos(self,numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma
     
        #! programa principal
        sumatoria=0
        num=int(input("Numero a procesar: "))
        while num!=0:
            print("Suma:", sumadigitos(num))
            sumatoria=sumatoria+num
            num=int(input("numero a procesar: "))
        print("Sumatoria:",sumatoria)
        print("digitos:",sumadigitos(sumatoria))

    def ejerVIDEO10_1_4(self):
        mayor=0
        numero=int(input("Numero primo: "))

        def primo(num):
            for i in range(2,num):
                if num%i==0:
                    return False
            return True

        def frecuencia(numero,digito):
            cantidad=0
            while numero!=0:
                ultdigito=numero%10
                if ultdigito==digito:
                    cantidad+=1
                numero=numero//10
            return cantidad

        def factorial(numero):
            f=1
            if numero!=0:
                for i in range (1,numero+1):
                    f=f*1
            return f

        def sumadigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10 
                suma=suma+digito
                numero=numero//10
            return suma

        while primo(numero):
            print("suma de los dijitos:",sumadigitos(numero))
            digito=int(input("digito: "))
            print("El", digito,"aparece",frecuencia(numero,digito),"veces")
            if numero>mayor:
                mayor=numero
            numero=int(input("Numero primo: "))  
        print("Factorial de",mayor,":",factorial(mayor))  
        
    def ejerVIDEO10_2(self):
        def primo(num):
            for i in range(2,numero):
                if numero%i==0:
                    return False
                return True
        #! programa principal
        numero = int(input("Numero: "))
        if primo(numero):
            print("Es primo")
        else:
            print("No es primo")

    def ejerVIDEO10_2_2(self):
        def factorial(n):
            f=1
            if n!=0:
                for i in range(1,n+1):
                    f=f*i
            return f
        cantidad=0
        num=int(input("Número (-1 para contar): "))
        while num!=-1:
            print("Factorial: ", factorial(num))
            cantidad+=1
            num=int(input("Número (-1 para contar): "))
        print("Se leyeron: ",cantidad,"números")

    def ejerVIDEO10_2_3(self):
        def sumaDigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma+=digito
                numero//=10
            return suma
        
        cantidad=0
        mayor=-1
        numero=int(input("Número positivo: "))
        while numero >=0:
            suma = sumaDigitos(numero)
            if suma > mayor:
                mayor = suma
                n_mayorsuma = numero
            if suma < 10:
                cantidad+=1
            numero = int(input("Número positivo: "))
        print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
        print("Cantidad con sumatoria menor a 10:",cantidad)
    
    def ejerVIDEO10_3(self):
        def coordenadaZ(x,y):
            x+=10
            y+=15
            return x+y
        #! programa principal
        x = int(input("Coordenada eje x: "))
        y = int(input("Coordenada eje y: "))
        for i in range(3):
            z = coordenadaZ(x,y)
            x+=1
            y+=1
        print(x," . ",y)

    def ejerVIDEO10_3_1(self):
        def maximo(a,b):
            if a > b:
                return a
            else:
                return b

        def minimo(a,b):
            if a < b:
                return a 
            else:
                return b
        #! programa principal
        
        x = int(input("Un número: "))
        y = int(input("Otro número: "))
        print(maximo(x-3, minimo(x+2, y-5)))

    def ejerVIDEO10_4(self):
        def DNIvalido(dni):
            cantidad=0
            while dni != 0:
                cantidad+=1
                dni//=10
            return cantidad == 7 or cantidad ==8
        print(DNIvalido(340))
        print(DNIvalido(12345678))

    def ejerVIDEO10_4_2(self):
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud == 0:
                return 0
            cantidad = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    cantidad+=1
                else:
                    if cadena[i] == " " and i<(longitud-1) and cadena[i+1] != " ":
                        cantidad = 0
            return cantidad

        print(lenUltimaPalabra("hola soy"))

    def ejerVIDEO10_4_3(self):
        def DNIvalido(dni):
            cantidad=0
            while dni != 0:
                cantidad+=1
                dni//=10
            return cantidad == 7 or cantidad ==8
        
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud == 0:
                return 0
            cantidad = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    cantidad+=1
                else:
                    if cadena[i] == " " and i<(longitud-1) and cadena[i+1] != " ":
                        cantidad = 0
            return cantidad

        def primerosTresDigitos(numero):
            while numero >= 1000:
                numero /= 10
            return(int(numero))

        def obtenerIdentificador(nombre,dni):
            nombre=nombre.strip()
            i = nombre[0:nombre.find(" ")]
            i=i+str(lenUltimaPalabra(nombre))
            i = i + str(primerosTresDigitos(dni))
            return i

        nombre=input("Nombre del socio: ")
        while nombre != "":
            dni = int(input("DNI del socio: "))
            while not(DNIvalido(dni)):
                print("Número inválido")
            dni = int(input("DNI del socio: "))
            identificador=obtenerIdentificador(nombre,dni)
            print("El identificador del socio es: ",identificador)
            nombre= input("Nombre del socio: ")

    def ejerVIDEO11_1(self):
        L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]
        print('L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]')
        print('1. Cuál de estos elementos pertenecen a ella?\n85.7    0   True    [True]    85    "a"    [1,2,3]\n')    
        S = [85.7, 0, True, [True], [(0,0,1)], 85, "a", [1,2,3]]
        for i in S:
            if i in L:
                print(i,"si está en L",)
        
        print("\n2. Cómo obtener la posición en que se encuentra el elemento (0,0,1)?")
        print('L.index((0,0,1))', "=",L.index((0,0,1)))
        
        print("3. Cómo eliminar el último elemento, independientemente de cuántos elementos haya en la lista?")
        print('L.pop(len(L)-1)',"=", L.pop(len(L)-1),"\n",L)
 
        print('4. Utilizar una operación para contar cuántas veces aparece el string "a"')
        print('L.count("a")',"=",L.count("a"))        

    def ejerVIDEO11_1_2(self):
        def sumatoria(lista):
            suma = 0
            for n in lista:
                suma+= n
            return suma

        def numerosMenores(lista, limite):
            nueva = []
            for n in lista:
                if n < limite:
                    nueva.append(n)
            return nueva

        def frecuencias(lista):
            nueva=[]
            for n in lista:
                if (n, lista.count(n)) not in nueva:
                    nueva.append((n, lista.count(n)))
            return nueva

        #!1
        numeros=[]
        nro=int(input("Número: "))
        while nro != 0:
            numeros.append(nro)
            nro=int(input("Número: "))
        #!2
        eliminar = int(input("Número a eliminar: "))
        if eliminar in numeros:
            numeros.remove(eliminar)
        else:
            print("Ese número no está entre los ingresados")
        #!3
        print("Sumatoria de los números: ", sumatoria(numeros))
        #!4
        limite=int(input("Filtrar números menores a: "))
        for n in numerosMenores(numeros, limite):
            print(n)
        #!5
        print("Frecuencias:")
        for tupla in frecuencias(numeros):
            print(tupla[0], "aparece", tupla[1], "veces")

    def ejerVIDEO11_2(self):
        def agregarPasajeros(pasajeros):
            nombre = input("Nombre -x para cortar: ")
            while nombre != "x":
                dni=int(input("DNI: "))
                destino = input("Ciudad destino: ")
                pasajeros.append((nombre, dni, destino))
                nombre = input("Nombre -x para cortar: ")
            return pasajeros

        def agregarCiudades(ciudades):
            ciudad = input("Ciudad -x para cortar: ")
            while ciudad != "x":
                pais = input("Pais: ")
                ciudades.append((ciudad,pais))
                ciudad = input("Ciudad -x para cortar: ")
            return ciudades

        def buscarCiudad(pasajeros, dni):
            for viaje in pasajeros:
                if viaje[1]==dni:
                    return viaje[2]
            return ""

        def cantidadPasajerosCiudad(pasajeros, ciudad):
            cantidad = 0
            for viaje in pasajeros:
                if viaje[2] == ciudad:
                    cantidad+=1
            return cantidad

        def buscarPaisDestino(pasajeros, ciudades, dni):
            ciudadBuscada=buscarCiudad(pasajeros, dni)
            for ciudad in ciudades:
                if ciudad[0] == ciudadBuscada:
                    return ciudad[1]
            return ""

        def cantidadPasajerosPais(pasajeros, ciudades, pais):
            cantidad = 0
            for viaje in pasajeros:
                if pais == buscarPaisDestino(pasajeros, ciudades, viaje[1]):
                    cantidad+=1
            return cantidad

        pasajeros =[("Manuel Juarez", 12345678, "Liverpool"),("Silvana Paredes", 22709128, "Buenos Aires"),("Rosa Ortiz", 12534563, "Inglaterra")]
        ciudades = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]
        while True:
            print("1. Agregar pasajeros\n2. Agregar ciudades \n3. Buscar ciudad destino mediante el DNI \n4. Cantidad de pasajeros que viajan a una ciudad \n5. Buscar país destino mediante DNI \n6. Cantidad de pasajeros que viajan a un país\n7. Salir del programa")
            opcion = int(input("Acción a ejecutar: "))
            if opcion == 1:
                print("AGREGAR PASAJEROS")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion == 2:
                print("AGREGAR CIUDADES")
                ciudades=agregarCiudades(ciudades)
            elif opcion == 3:
                dni=int(input("DNI: "))
                print("El pasajero viaja a", buscarCiudad(pasajeros, dni))        
            elif opcion == 4:
                ciudad = input("Ciudad: ")
                print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad),"pasajeros")
            elif opcion == 5:
                dni = int(input("DNI: "))
                print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
            elif opcion == 6:
                pais=input("País: ")
                print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais),"pasajeros")
            elif opcion == 7:
                break

    def ejerVIDEO12_1(self):
        A={"z", 8, "9",(10,20,30),8,9,8}
        B={7,8,9}
        print('\n Dados los siguientes conjuntos: \nA={"z", 8, "9",(10,20,30),8,9,8}\nB={7,8,9}\n¿Cuántos elementos tiene el conjunto A?')
        print(len(A))

        print('\n¿Cómo se podrían agregar en el conjunto B los números 1, 2, 3, en una única operación?')
        print('B.update([1,2,3])', "=", B.update([1,2,3]))

        print("\n¿Es A menor que B o B menor que A?\nNinguna de las dos. Cada uno tiene elementos únicos")

    def ejerVIDEO12_1_2(self):
        def cargarNombres(alumnos):
            nombre = input("Nombre: ")
            while nombre != "x":
                alumnos.add(nombre)
                nombre= input("Nombre: ")
            return alumnos

        primaria = set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria = cargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria = cargarNombres(secundaria)

        print("NOMBRES DE TODOS LOS ALUMNOS: ")
        for nombre in primaria|secundaria:
            print(nombre)

        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)

        print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA")
        for nombre in primaria-secundaria:
            print(nombre)

    def ejerVIDEO12_1_3(self):
        def direcciones(ventas):
            domicilios=set()
            for venta in ventas:
                domicilios.add(venta[3])
            return domicilios
        
        direcc = [("Nuria Costa", 5, 12790.78, "Calle las Flores 355"), ("Jorge Russo", 7, 669, "Mirasol 218"), ("Nuria Costa", 9, 532.90, "Calle las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
        print(direcciones(direcc))

    def ejerVIDEO13_1(self):
        E = {1:"a", "prueba":[1,2,3,5], (4,5):3}
        print('Dado el siguiente diccionario:\n E = {1:"a", "prueba":[1,2,3,5], (4,5):3}')
        print("\n¿Es el 1 un elemento de E?\n No, los elementos sólo pueden ser pares formados por clave: valor")

        print("\n¿Cuántos elementos tiene E?\nTiene 3 elementos")

        print("\n¿Por qué da error la instrucción E[0]?\nPorque la clave 0 no existe en E")

        print('¿Qué retorna la instrucción 1 en E.values0()?\nFalse, El número 1 existe como clave y también existe dentro de la lista E["prueba"] pero no existe entre los valores del diccionario E')

        print('\n¿Qué retorna E["prueba"][2] y por qué?\n3, porque E["prueba"] es una lista y su posición 2 almacena al número 3')

    def ejerVIDEO13_1_2(self):
        contadores = {}
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        for letra in alfabeto.upper():
            contadores[letra] = 0
        for i in range(3):
            cadena = input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() in alfabeto:
                    contadores[caracter]+=1
        
        for caracter,cantidad in contadores.items():
            print(caracter, ":", cantidad)

    def ejerVIDEO13_1_3(self):
        def funcion1(pacientes):
            e=0
            t=0
            for datos in pacientes.values():
                if datos[2]:
                    e+=datos[1]
                    t+=1
            if t>0:
                return e/t
            else:
                return 0

        def funcion2(pacientes, medicos, dni):
            for medico in medicos:
                if medico[0] == pacientes[dni][3]:
                    return medico[1]
            return ""
        pacientes = {10267489:["Marta Ramos",68,True,829], 22819922: ["Lucas Pérez", 47, False, 437], 40526661: ["Facundo Lucero", 29, True, 829]}
        print(funcion1(pacientes))
        medicos = {(829,"Gabriela Ríos"),(437, "Pedro Olivares"), (561, "Soledad Fuentes")}
        print(funcion2(pacientes,medicos,22819922))

    def ejerVIDEO13_2(self):
        def cargarSocios(socios):
            numero = int(input("Número de socio:"))
            while numero != 0:
                nombre = input("Nombre y apellido: ")
                fecha = input("Fecha de ingreso: ")
                cuota = input("Cuota al día s/n: ")
                pago = cuota.lower() == "s"
                socios[numero] = [nombre,fecha,pago]
                numero = int(input("Número de socio: "))
            return socios 
    
        def modificarFecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]= fecha_nueva
            return socios

        def numeroSocio(socios,nombre):
            for numero, datos in socios.items():
                if datos[0].lower() == nombre.lower():
                    return numero
            return 0

        def formatoFecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
            for numero, datos in socios.items():
                print("-Número: ",numero)
                print("-Nombre: ",datos[0])
                print("-Fecha de ingreso: ",formatoFecha(datos[1]))
                if datos[2]:
                    print("-Cuota al día")
                else:
                    print("-En deuda")
                print("~~~~~~~~~~~~")
            return None
        socios_activos={1:["Amanda Núñez", "17032009", True], 2:["Bárbara Molina","17032009"], 3:["Lautaro Campos","17032009"]}
        print("***Cargar Socios")
        socios_acitvos=cargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero = int(input("Número de socio: "))
        socios_activos[numero][2] = True

        print("***Modificando fecha de ingreso...")
        socios_activos = modificarFecha(socios_activos, "13032018", "14032018")
        
        print("***Eliminar socio: ")
        nombre = input("Nombre y Apellido: ")
        numero = numeroSocio(socios_activos, nombre)
        del socios_activos[numero]

        imprimirListado(socios_activos)

ejecutar=ejerciciosTAREA2()
ejecutar.ejerVIDEO13_2()
