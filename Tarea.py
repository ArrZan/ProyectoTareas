from types import coroutine


class Ejercicios:
    def Ejercicio1_4(self):
        a = int(input("ingrese 1er numero: "))
        b = int(input("ingrese 2do numero: "))
    
        s = a+b
        r = a-b
        m = a*b
        d = a/b
        mod = a%b
        print("La suma es {}, la resta es {}, la multiplicación {}, la división {} y el módulo {}.".format(s,r,m,d,mod))
    
    def Ejercicio1_5(self):
        a = int(input("ingrese 1er numero: "))
        b = int(input("ingrese 2do numero: "))
        c = int(input("ingrese 3er numero: "))

        r1 = (-b + (((b**2)-(4*a*c))**(0.5)))/(2*a)
        r2 = (-b - (((b**2)-(4*a*c))**(0.5)))/(2*a)

        print("Sus valores son:{} y {}".format(r1,r2))

    def Ejercicio1_6(self):
        
        a = int(input("Ingrese 1er lado en cm: "))
        b = int(input("Ingrese 2do lado en cm: "))

        h = (((a**2)+(b**2))**(0.5)) 

        print("Su hipotenusa es: ",h)

    def Ejercicio1_7(self):
    
        a = int(input("Ingrese un número: "))
        r = a%2
        
        if r == 0:
            print("0")
        else:
            print("1")
        
    def Ejercicio1_9(self):
        n = input("Ingrese un número binario de 4 dígitos: ")

        b = int(n[0]) + int(n[1]) + int(n[2])+ int(n[3])

        rb = b%2
        if rb == 0:
            n = n + "0"
        else:
            n = n + "1"
        print(n)

    def Ejercicio1_10(self):
        a = input("Ingrese número binario de cuatro dígitos: ")
        print(a)
        b = ((2*(int(a[0])))**3) + ((2*(int(a[1])))**2) + ((2*(int(a[2])))**1) + ((2*(int(a[3])))**0)
        print(b)

    def Ejercicio1_11(self):
        n = input("Ingrese número binario de cuatro dígitos: ")

        print("Unidades: ",(n[3]))
        print("Decenas: ",(n[2]))
        print("Centenas: ",(n[1]))
        print("Unidades de mil: ",(n[0]))
        
    def Ejercicio2_1(self):
        a = int(input("Ingrese fecha (ddmmaaaa): "))
        b = str(a)
        c = int(b[4] + b[5] + b[6] + b[7])
        lb = [(c%400),(c%4),(c%100)]
        
        res = False
        if lb[1] == 0 and not(lb[2] == 0):
            res = True

        if lb[0] == 0 or res:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")

    def Ejercicio2_3(self):
        a = int(input("Ingrese un número de 5 dígitos: "))
        b = str(a)
    
        if b[0] == b[4] and b[1] == b[3]:
            print("Es un número capicúa.")
        else:
            print("No es número capicúa")

    def Ejercicio2_4(self):
        h = int(input("Ingrese las horas: "))
        m = int(input("Ingrese los minutos: "))
        print("Su resultado es: {} segundos",((h*3600)+(m*60)))

    def Ejercicio2_5(self):
        a = int(input("Ingrese valor (segundos): "))
        while a <= 0:
            a = int(input("Por favor ingrese un valor positivo (segundos): "))
        
        b = [(a/60),(a/3600),(a/86400)]

        print("Su equivalente en minutos es {}, en horas {} y en días {}.".format(b[0],b[1],b[2]))

    def Ejercicio2_6(self):
        ns = [0]*3
        ab = ["primer","segundo","tercer"]
        ct= 0

        while ct <= 2:
            ns[ct] = int(input("Ingrese "+ ab[ct] + " número: "))
            ct= ct + 1
        
        if ns[0] > ns[1] and ns[0] > ns[2]:
            pn = ns[0]
            if ns[1] > ns[2]:
                sn = ns[1]
            else: 
                sn = ns[2]
        else:
            if ns[1] > ns[0] and ns[1] > ns[2]:
                pn = ns[1]
                if ns[0] > ns[2]:
                    sn = ns[0]
                else:
                    sn = ns[2]
            else:
                pn = ns[2]
                if ns[0] > ns[1]:
                    sn = ns[0]
                else:
                    sn = ns[1]

        print("El primer valor mayor es {} y el segundo mayor es {}.".format(pn,sn))

    def Ejercicio2_7(self):
        t1 = [0, 0, "", 0, 0, ""]
        t2 = [0]*2
        pbs = ["la hora de entrada", "los minutos excedentes de entrada", 2, "la hora de salida", "los minutos excedentes de salida", 5]
        ct = 0

        for i in pbs:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    t1[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                a = input("La hora que ingresó es AM o PM? ")
                t1[(pbs[ct])] = a
        
        t2[0] = (t1[0] * 3600) + (t1[1] * 60)
        t2[1] = (t1[3] * 3600) + (t1[4] * 60)

        if t1[2] == t1[5]:
            nhp = t2[1] - t2[0]
        else:
            nhp = (43200 - t2[0]) + t2[1]
        
        t2[0] = (nhp-(nhp % 3600)) / 3600
        t2[1] = (nhp%3600)/60
        print(t2)
        mp = t2[0] * 4

        if t2[1] >= 30:
            mp = mp + 2.50
        print("El dueño del vehículo pagará Bs. ",mp)    

    def Ejercicio2_8(self):
        Cl = ["no cumple con el Criterio de ingreso", "tiene infra peso", "tiene bajo peso", "tiene peso normal", "tiene sobrepeso", "tiene obesidad pre-mórbida", "tiene obesidad mórbida","tiene obesidad híper-mórbida"]
        mi = int(input("Ingrese su peso en libras: "))
        et = int(input("Ingrese su estatura en centímetros: "))
        
        imc = (mi * 0.453592) / ((et*0.01)**2)

        if imc > 45:
            i = Cl[7]
        elif imc > 40:
            i = Cl[6]
        elif imc > 30:
            i = Cl[5]
        elif imc > 25:
            i = Cl[4]
        elif imc > 18.5:
            i = Cl[3]
        elif imc > 17:
            i = Cl[2]
        elif imc > 16:
            i = Cl[1]
        else:
            i = Cl[0]
        
        print("Su peso en kilogramos es {} y por ende su IMC es de {} que significa que {}.".format((mi*0.453592), imc, i))

    def Ejercicio2_9(self):
        ma = {"ENERO": 31, "FEBRERO": 59, "MARZO": 90, "ABRIL": 120, "MAYO": 151, "JUNIO": 181, "JULIO": 212, "AGOSTO": 243, "SEPTIEMBRE": 273, "OCTUBRE": 304, "NOVIEMBRE": 334, "DICIEMBRE": 365}
        fcd = int(input("Ingrese el día: "))
        fcm = input("Ingrese el mes: ").upper()
    
        for i in ma:   
            if i == fcm:
                print("Han pasado {} días.".format(((ma[i])+fcd)))

    def Ejercicio2_10(self):
        ms = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8, "Septiembre":9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12}

        ns = int(input("Ingrese un número del 1 al 12: "))

        for i in ms:
            if ns == ms[i]:
                print("Su mes es ",i)

    def Ejercicio3_1(self):
        mp = int(input("Ingrese su monto a pagar: "))
        t = mp
        if mp > 1000:
            t = t - (mp * 0.2)
        print("Su monto a pagar es Bs ",t)

    def Ejercicio3_1(self):
        a = int(input("Ingrese su número: "))
        a = str(a)
        print("{} tiene {} dígitos".format(a, len(a)))

    def Ejercicio3_2(self):
        nc = int(input("Ingrese su número: "))
        t = True
        cti = 0
        nc = str(nc)
        ctf = len(str(nc)) - 1
        
        while t:
            if ctf - cti == 1 or ctf - cti == 2:
                t = False
    
            if nc[cti] == nc[ctf]:
                det = True
            else:
                det = False
            cti += 1
            ctf -= 1
        
        if det:
            print("Es un número capicúa.")
        else:
            print("No es un número capicúa.")

    def Ejercicio3_3(self):
        n = int(input("Ingrese un número: "))
        i = "no es primo"

        if n%2 != 0:
            i = "es primo"
        print("El número ingresado",i)

    def Ejercicio3_4(self):
        nf = int(input("Ingrese número factorial "))
        r = 1
        for i in range(1, nf+1, 1):
            r = i * r
        print(r)

    def Ejercicio3_5(self):
        nc = 0
        r = True
        while r:
            if len((str(nc))) < 10: 
                nc = int(input("Ingrese la contraseña: "))
                if len((str(nc))) == 10:
                    r = False
        print("Su contraseña cumple con la seguridad exitosamente!")

    def Ejercicio3_6(self):
        a = 1
        ct = -1
        b = []
        vm = 0
        vmn = vm
        while a != 0:
            a = int(input("Ingrese un número: "))
            b.append(a)
            ct += 1
            if ct == 1:
                if a > vm:
                    vmn = vm
                    vm = a
                else:
                    vmn = a
            elif ct ==0:
                vm = b[0]
            
            if ct >= 1:
                if a != 0:
                    if a > vm:
                        vm = a       
                    if a < vmn:
                        vmn = a
                else:
                    break

        print("El número menor es {} y el número mayor es {}.".format(vmn,vm))


    def Ejercicio3_7(self):
        a = 0
        p = ["La edad", "El peso(kg)", "La estatura(cm)"]
        lm = [24, 74, 182, 30, 70, 170, 41, 60, 169, 22, 75, 183, 31, 83, 178, 35, 76, 172, 22, 68, 164, 23, 77, 163,
            23, 58, 163, 26, 89, 185, 23, 55, 162, 26, 47, 160, 26, 60, 163, 22, 54, 170, 23, 58, 165, 26, 75, 178,
            24, 65, 170, 28, 82, 177, 42, 85, 183, 25, 75, 174, 35, 53, 150, 19, 60, 169, 35, 59, 160, 45, 74, 162,
            40, 58, 160, 33, 69, 167, 55, 70, 158, 24, 64, 160, 29, 79, 180, 52, 69, 160, 42, 78, 169, 34, 63, 152, 0] #96 pf
        per = [0, 0, 0,0]
        ac = [0, 0, 0]
        ct = 0
        while a < 3: # 3 para control de posición de lista acumulador
            ac[a] = ac[a] + lm[ct]
            
            if lm[ct] == lm[96] or lm[ct] == lm[95] or lm[ct] == lm[94]:
                a += 1
                ct = 0
                ct += a
            else:
                if a == 0:
                    if lm[ct]>18 and lm[ct]<25:
                        per[0] += 1
                        per[3] += lm[ct+1]
                elif lm[ct]>36:
                        per[1] += 1
                ct += 3
        
        for i in p:
            ct+=1
            print("{} promedio de todas las personas en la muestra es {}".format(i,round(((ac[ct-4])/32))))

        print("Hay {} personas con edad entre los 18 y 25 años con un peso promedio de {}".format(per[0],round((per[3]/per[0]))))
        print("Hay {} personas mayores a 36 años".format(per[1]))


    def Ejercicio3_8(self):
        for i in range(1, 11, 1):
            for j in range (1, 13, 1):
                print("{} * {} = {}".format(i, j, (i*j)))
            print("*"*34)

    def Ejercicio3_9(self):
        a = 0
        ct = 0

        for i in range(0, 7, 1):
            for j in range(i,7,1):
                print(i," ", j) 
            
    def Ejercicio3_10(self):
        n = 1
        t = 0
        ct = 0
        a = ["Ingrese", "Error, Ingrese"]
        b = 0
        while n != 0:
            n = int(input(a[b] + " un número positivo: "))
            if n>1:
                b = 0
                t += n
                ct += 1
            else:
                b = 1

        print("Su promedio de la serie dada es: ",(t/(ct)))

    def Ejercicio4_1(self):
        ban = input("Desea ingresar datos? sí (y) o no (n) ")
        
        if ban.lower() == "y":
            print("Si desea salir, ingrese una 'x'")
            prom = Ejercicios()
            pro = prom.SoliUser(ban)
            if pro != 0:
                print("El promedio de las edades mayores a 18 años es: ",pro)
            elif pro == 0:
                print("No hay edades mayores a 18 años.")
            else:
                print("Dado que no ha dado valores, no hay promedio.")
        else:
            print("Ha salido!")

    def SoliUser(self,a):
        le = []
        while a.lower() != "x":
            b = input("Ingrese edad: ")
            if b == "x":
                a = "x"
            elif b != "x" and int(b) <= 0:
                print("Ingrese un valor acorde por favor, o 'x' para dejar de ingrear datos.")
            elif int(b) > 18:
                le.append(int(b))
                

        if len(le) > 0:
            print(le)
            pr = (sum(le))/len(le)
        else:
            pr = 0
        
        return pr

    def Ejercicio4_2(self):
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese su exponente: "))
        exp = Ejercicios()
        ex = exp.Eleva(a,b)
        print("El resultado de elevar {} a la {} es {}".format(a,b,ex))
        
    def Eleva(self,ba,ex):
        re = ba**ex
        return re

    def Ejercicio4_3(self):
        # Ejercicio 3.
        # Escriba una función que calcule el perímetro del pentágono (siendo el
        # perímetro la suma de los lados del polígono).
        la = int(input("Ingrese el lado del polígono: "))
        per = Ejercicios()
        pe = per.PerPenta(la)
        print("El perímetro del pentágono es: {}".format(pe))
        
    def PerPenta(self,la):
        res = la*5
        return res

    def Ejercicio4_4(self):
        id = {}
        acp = Ejercicios()

        while len(id) <= 4:
            a = input("Ingrese su identificación(nombre): ")
            id[a] = int(input("Ingrese horas trabajadas{}: ".format(a)))
        th = int(input("Ingrese el monto por hora: "))

        ss = acp.CalSalSem(id,th)
        for i in ss:
            print(i,"cobrará",ss[i][1])

    def CalSalSem(self,a,re):
        Cacp = Ejercicios()
        for i in a:
            if a[i] <= 40:
                a[i] = [a[i],(a[i]*re)]
            else:
                a[i] = [a[i],(40*re)]
                a[i][1] = Cacp.CalIngHExt(a[i],re)
        print("*"*20)
        return a

    def CalIngHExt(self,k,et):
        extr = k[1] + ((k[0]-40) *(et + (et * 0.35)))
        return extr

    def Ejercicio4_5(self):
        # ac = "Ciudad A"
        # bc= "Ciudad B"
        # ccd = 332
        Cal = Ejercicios()
        # Cmk = Cal.Calmikm(ac,bc,ccd)
        # print("Entre la {} y la {} hay {} Km".format(ac,bc,round(Cmk,2)))
        
        dp = ["primer","segundo","tercer","cuarto"]
        ct = 0
        while ct < 5:
            ac = input("Ingrese el {} par de Ciudad:\n1. ".format(dp[ct]))
            bc = input("2. ")
            ccd = int(input("Ingrese la distancia entre la ciudad {} y {}: ".format(ac,bc)))
            # co.append(ac)
            # cd.append(bc)
            Cmk = Cal.Calmikm(ac,bc,ccd)
            print("Entre la ciudad de {} y la de {} hay {} Km".format(ac,bc,round(Cmk,2)))
            ct+=1

    def Calmikm(self,a,b,c):
        kmc = 1.60935
        res = c * kmc
        return res


sauce = Ejercicios()
sauce.Ejercicio4_5()
