import time
def mesi(f,f_prima,x):
    if ((f / f_prima) < 0):
        res = x + ((-1) * (f / f_prima))
    else:
        res = x - (f / f_prima)
    return (res)

r=0.00000304042

x=1



for i in range(560000):

    f = (x**5) - (2*(x**4)) - (r*(x**4)) + (x**3) + (2*r*(x**3)) - (x**2) - (r*(x**2)) + (2*x) - (2*r*x) + r - 1 - (2*r*(x**2))

    f_prima = (5 * (x**4)) - (8 * (x**3)) - (4 * r *(x**3)) + (3*(x**2)) + (6*r*(x**2)) -(2*x) - (2*r*x) - (2*r) + 3
    print(mesi(f,f_prima,x))
    x=mesi(f,f_prima,x)

