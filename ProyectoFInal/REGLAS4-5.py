# R E G L A 4 ----------
puentes = [("p", T[0]), ("q", T[0]), ("s",T[0]), ("r", T[0]), ("u", T[0]), ("t", T[0]), ("y", T[0]), ("x", T[0]), ("b", T[0]), ("c", T[0])]
n_puentes = [("p", T[0]), ("q", T[0]), ("s",T[0]), ("r", T[0]), ("u", T[0]), ("t", T[0]), ("y", T[0]), ("x", T[0]), ("b", T[0]), ("c", T[0])]

atomoP = caminos.P([0,0,0]) #Ā
atomoQ = caminos.P([0,0,1]) #ę
atomoS = caminos.P([1,0,0]) #ā
atomoR = caminos.P([1,0,1]) #Ě
atomoU = caminos.P([2,0,0]) #Ă
atomoT = caminos.P([2,0,1]) #ě
atomoX = caminos.P([3,0,0]) #ă
atomoY = caminos.P([3,0,1]) #Ĝ
atomoB = caminos.P([4,0,0]) #Ą
atomoC = caminos.P([4,0,1]) #ĝ

p = caminos.escribir(atomoP)
q = caminos.escribir(atomoQ)
r = caminos.escribir(atomoR)
s = caminos.escribir(atomoS)
t = caminos.escribir(atomoT)
u = caminos.escribir(atomoU)
x = caminos.escribir(atomoX)
y = caminos.escribir(atomoY)
b = caminos.escribir(atomoB)
c = caminos.escribir(atomoC)

msn = ""

for i in range(Nx-1):
    opc = random.choice(n_puentes)
    if opc == ("p",T[0]):
        msn += "{0} y {1} ".format(p, s)
    
    elif opc == ("q",T[0]):
        msn += "{0} Y ({1} o {2}) ".format(q,y,b)
    
    elif opc == ("s",T[0]):
        msn += "{0} Y ({1} o {2}) ".format(s,x,t)

    elif opc == ("r", T[0]):
        msn += "{0} Y {1} ".format(r,q)

    elif opc == ("u",T[0]):
        msn += "{0} Y ({1} O {2}) ".format(u,x,r)
    
    elif opc == ("t", T[0]):
        msn += "{0} Y {1} ".format(t,c)
    
    elif opc == ("y",T[0]):
        msn += "{0} Y ({1} o {2}) ".format(y,r,t)

    elif opc == ("x",T[0]):
        msn += "{0} Y ({1} o el sentido{2}) ".format(x,p,b)

    elif opc == ("b", T[0]):
        msn += "{0} Y {1} ".format(b, u)
    
    elif opc == ("c",T[0]):
        msn += "{0} Y ({1} O {2}) ".format(c,y,p)
    
    n_puentes.remove(opc)
    
print(msn)
#print(caminos.escribir(atomoP)

# R E G L A 5 - - - - - - - - - - - - - - - 
atomoP = caminos.P([0,0,0]) #Ā
atomoQ = caminos.P([0,0,1]) #ę
atomoS = caminos.P([1,0,0]) #ā
atomoR = caminos.P([1,0,1]) #Ě
atomoU = caminos.P([2,0,0]) #Ă
atomoT = caminos.P([2,0,1]) #ě
atomoX = caminos.P([3,0,0]) #ă
atomoY = caminos.P([3,0,1]) #Ĝ
atomoB = caminos.P([4,0,0]) #Ą
atomoC = caminos.P([4,0,1]) #ĝ

p = caminos.escribir(atomoP)
q = caminos.escribir(atomoQ)
r = caminos.escribir(atomoR)
s = caminos.escribir(atomoS)
t = caminos.escribir(atomoT)
u = caminos.escribir(atomoU)
x = caminos.escribir(atomoX)
y = caminos.escribir(atomoY)
b = caminos.escribir(atomoB)
c = caminos.escribir(atomoC)

msn = ""
opcs = [p,q,r,s,t,u,x,y,b,c]

for i in opcs:
    posibilidad = random.choice(opcs)
    if posibilidad == p:
        msn += "({0} O NO({1})) ".format(p,q)
    elif posibilidad == q:
        msn += "({0} O NO({1})) ".format(q,p)
    elif posibilidad == r:
        msn += "({0} O NO({1})) ".format(r,s)
    elif posibilidad == s:
        msn += "({0} O NO({1})) ".format(s,r)
    elif posibilidad == t:
        msn += "({0} O NO({1})) ".format(t,u)
    elif posibilidad == u:
        msn += "({0} O NO({1})) ".format(u,t)
    elif posibilidad == x:
        msn += "({0} O NO({1})) ".format(x,y)
    elif posibilidad == y:
        msn += "({0} O NO({1})) ".format(y,x)
    elif posibilidad == b:
        msn += "({0} O NO({1})) ".format(b,x)
    elif posibilidad == c:
        msn += "({0} O NO({1})) ".format(c,b)
print(msn)

#aqui abajo es una forma mas corta, pero es el mismo codigo que el de arriba 
msn1 = ""
for i in opcs:
    posibilidad = random.choice(opcs)
    if posibilidad == p:
        msn1 += "({0} O NO({1})) ".format(atomoP,atomoQ)
    elif posibilidad == q:
        msn1 += "({0} O NO({1})) ".format(atomoQ,atomoP)
    elif posibilidad == r:
        msn1 += "({0} O NO({1})) ".format(atomoR,atomoS)
    elif posibilidad == s:
        msn1 += "({0} O NO({1})) ".format(atomoS,atomoR)
    elif posibilidad == t:
        msn1 += "({0} O NO({1})) ".format(atomoT,atomoU)
    elif posibilidad == u:
        msn1 += "({0} O NO({1})) ".format(atomoU,atomoT)
    elif posibilidad == x:
        msn1 += "({0} O NO({1})) ".format(atomoX,atomoY)
    elif posibilidad == y:
        msn1 += "({0} O NO({1})) ".format(atomoY,atomoX)
    elif posibilidad == b:
        msn1 += "({0} O NO({1})) ".format(atomoB,atomoC)
    elif posibilidad == c:
        msn1 += "({0} O NO({1})) ".format(atomoC,atomoB)
print(msn1)