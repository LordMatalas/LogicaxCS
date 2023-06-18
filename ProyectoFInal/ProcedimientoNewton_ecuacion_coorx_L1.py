
a = 1

def f(x):
    
    r=3.04042*(10**-6)
    y= (x**5)-(2+r)*(x**4) + (1+(2*r))*(x**3)-(1-r)*(x**2) + 2*(1-r)*x + r - 1
    
    return y

def df(x):
    
    r=3.04042*(10**-6)
    dy =5*(x**4)-((8+(4*r))*x**3)+((3+(6*r))*(x**2))-((2-(2*r))*x)+2-(2*r)
    return dy

def Newton(x):

    cualquiera = x - (f(x)/df(x))

    return cualquiera

contador = 1
for i in range(20):
    print(contador, end="  ")
    print(Newton(a))
    a=Newton(a)
    contador +=1

