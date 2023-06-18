# r e g l a 4 - - - - - - - - - - - - - - - - - 

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

#forma distinta
regla4_p = "("+"("+"("+caminos.P([0,0,0])+"O"+caminos.P([0,1,0])+")"+"O"+"("+caminos.P([0,2,0])+"O"+caminos.P([0,3,0])+")"+")"+">"+"("+"("+caminos.P([1,1,0])+"O"+caminos.P([1,2,0])+")"+"O"+"("+caminos.P([1,3,0])+"O"+caminos.P([1,4,0])+")"+")"+")"
regla4_y = "("+"("+"("+caminos.P([3,0,1])+"O"+caminos.P([3,1,1])+")"+"O"+"("+caminos.P([3,2,1])+"O"+caminos.P([3,3,1])+")"+")"+">"+"("+"("+"("+caminos.P([1,1,1])+"O"+caminos.P([1,2,1])+")"+"O"+"("+caminos.P([1,3,1])+"O"+caminos.P([1,4,1])+")"+")"+"O"+"("+"("+caminos.P([2,1,1])+"O"+caminos.P([2,2,1])+")"+"O"+"("+caminos.P([2,3,1])+"O"+caminos.P([2,4,1])+")"+")"+")"+")"
regla4_b = "("+"("+"("+caminos.P([4,0,0])+"O"+caminos.P([4,1,0])+")"+"O"+"("+caminos.P([4,2,0])+"O"+caminos.P([4,3,0])+")"+")"+">"+"("+"("+caminos.P([2,1,0])+"O"+caminos.P([2,2,0])+")"+"O"+"("+caminos.P([2,3,0])+"O"+caminos.P([2,4,0])+")"+")"+")"
regla4_q = "("+"("+"("+caminos.P([0,0,1])+"O"+caminos.P([0,1,1])+")"+"O"+"("+caminos.P([0,2,1])+"O"+caminos.P([0,3,1])+")"+")"+">"+"("+"("+"("+caminos.P([3,1,1])+"O"+caminos.P([3,2,1])+")"+"O"+"("+caminos.P([3,3,1])+"O"+caminos.P([3,4,1])+")"+")"+"O"+"("+"("+caminos.P([4,1,0])+"O"+caminos.P([4,2,0])+")"+"O"+"("+caminos.P([4,3,0])+"O"+caminos.P([4,4,0])+")"+")"+")"+")"
regla4_c = "("+"("+"("+caminos.P([4,0,1])+"O"+caminos.P([4,1,1])+")"+"O"+"("+caminos.P([4,2,1])+"O"+caminos.P([4,3,1])+")"+")"+">"+"("+"("+"("+caminos.P([3,1,1])+"O"+caminos.P([3,2,1])+")"+"O"+"("+caminos.P([3,3,1])+"O"+caminos.P([3,4,1])+")"+")"+"O"+"("+"("+caminos.P([0,1,0])+"O"+caminos.P([0,2,0])+")"+"O"+"("+caminos.P([0,3,0])+"O"+caminos.P([0,4,0])+")"+")"+")"+")"
regla4_x = "("+"("+"("+caminos.P([3,0,0])+"O"+caminos.P([3,1,0])+")"+"O"+"("+caminos.P([3,2,0])+"O"+caminos.P([3,3,0])+")"+")"+">"+"("+"("+"("+caminos.P([4,1,0])+"O"+caminos.P([4,2,0])+")"+"O"+"("+caminos.P([4,3,0])+"O"+caminos.P([4,4,0])+")"+")"+"O"+"("+"("+caminos.P([0,1,0])+"O"+caminos.P([0,2,0])+")"+"O"+"("+caminos.P([0,3,0])+"O"+caminos.P([0,4,0])+")"+")"+")"+")"
regla4_s = "("+"("+"("+caminos.P([1,0,0])+"O"+caminos.P([1,1,0])+")"+"O"+"("+caminos.P([1,2,0])+"O"+caminos.P([1,3,0])+")"+")"+">"+"("+"("+"("+caminos.P([3,1,0])+"O"+caminos.P([3,2,0])+")"+"O"+"("+caminos.P([3,3,0])+"O"+caminos.P([3,4,0])+")"+")"+"O"+"("+"("+caminos.P([2,1,1])+"O"+caminos.P([2,2,1])+")"+"O"+"("+caminos.P([2,3,1])+"O"+caminos.P([2,4,1])+")"+")"+")"+")"
regla4_r = "("+"("+"("+caminos.P([1,0,1])+"O"+caminos.P([1,1,1])+")"+"O"+"("+caminos.P([1,2,1])+"O"+caminos.P([1,3,1])+")"+")"+">"+"("+"("+caminos.P([0,1,1])+"O"+caminos.P([0,2,1])+")"+"O"+"("+caminos.P([0,3,1])+"O"+caminos.P([0,4,1])+")"+")"+")"
regla4_u = "("+"("+"("+caminos.P([2,0,0])+"O"+caminos.P([2,1,0])+")"+"O"+"("+caminos.P([2,2,0])+"O"+caminos.P([2,3,0])+")"+")"+">"+"("+"("+"("+caminos.P([3,1,0])+"O"+caminos.P([3,2,0])+")"+"O"+"("+caminos.P([3,3,0])+"O"+caminos.P([3,4,0])+")"+")"+"O"+"("+"("+caminos.P([1,1,1])+"O"+caminos.P([1,2,1])+")"+"O"+"("+caminos.P([1,3,1])+"O"+caminos.P([1,4,1])+")"+")"+")"+")"
regla4_t = "("+"("+"("+caminos.P([2,0,1])+"O"+caminos.P([2,1,1])+")"+"O"+"("+caminos.P([2,2,1])+"O"+caminos.P([2,3,1])+")"+")"+">"+"("+"("+caminos.P([4,1,1])+"O"+caminos.P([4,2,1])+")"+"O"+"("+caminos.P([4,3,1])+"O"+caminos.P([4,4,1])+")"+")"+")"

p = [regla4_p,regla4_y,regla4_b,regla4_q,regla4_c,regla4_x,regla4_s,regla4_r,regla4_u,regla4_t]
res = Ytoria(p)

#E S T A S S O N P R U E B A S - - - - - - - - - - - - - - - - - -
#print(regla4_p)
#print(regla4_y)
#print(regla4_b)
#print(regla4_q)
#print(regla4_c)
#print(regla4_x)
#print(regla4_s)
#print(regla4_r)
#print(regla4_u)
#print(regla4_t)
#print(res)

#print(inorder_to_tree(regla4_p))
#print(inorder_to_tree(regla4_y))
#print(inorder_to_tree(regla4_b))
#print(inorder_to_tree(regla4_q))
#print(inorder_to_tree(regla4_c))
#print(inorder_to_tree(regla4_x))
#print(inorder_to_tree(regla4_s))
#print(inorder_to_tree(regla4_r))
#print(inorder_to_tree(regla4_u))
#print(inorder_to_tree(regla4_t))
#print(inorder_to_tree(res))

#print(tseitin(res))
#v = {}
#dpll(x,v)

# r e g l a 5 - - - - - - - - - - - - - - - - - - -- 
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

regla5_p = "("+"("+"("+caminos.P([3,0,0])+"O"+caminos.P([3,1,0])+")"+"O"+"("+caminos.P([3,2,0])+"O"+caminos.P([3,3,0])+")"+")"+"O"+"-"+"("+"("+caminos.P([4,1,1])+"O"+caminos.P([1,2,1])+")"+"O"+"("+caminos.P([4,3,1])+"O"+caminos.P([4,4,1])+")"+")"+")"
regla5_t = "("+"("+"("+caminos.P([2,0,1])+"O"+caminos.P([2,1,1])+")"+"O"+"("+caminos.P([2,2,1])+"O"+caminos.P([2,3,1])+")"+")"+"O"+"-"+"("+"("+caminos.P([4,1,0])+"O"+caminos.P([4,2,0])+")"+"O"+"("+caminos.P([4,3,0])+"O"+caminos.P([4,4,0])+")"+")"+")"
regla5_r = "("+"("+"("+caminos.P([1,0,1])+"O"+caminos.P([1,1,1])+")"+"O"+"("+caminos.P([1,2,1])+"O"+caminos.P([1,3,1])+")"+")"+"O"+"-"+"("+"("+caminos.P([0,1,0])+"O"+caminos.P([0,2,0])+")"+"O"+"("+caminos.P([0,3,0])+"O"+caminos.P([0,4,0])+")"+")"+")"
regla5_x = "("+"("+"("+caminos.P([3,0,0])+"O"+caminos.P([3,1,0])+")"+"O"+"("+caminos.P([3,2,0])+"O"+caminos.P([3,3,0])+")"+")"+"O"+"-"+"("+"("+caminos.P([0,1,1])+"O"+caminos.P([0,2,1])+")"+"O"+"("+caminos.P([0,3,1])+"O"+caminos.P([0,4,1])+")"+")"+")"
regla5_r1 = "("+"("+"("+caminos.P([1,0,1])+"O"+caminos.P([1,1,1])+")"+"O"+"("+caminos.P([1,2,1])+"O"+caminos.P([1,3,1])+")"+")"+"O"+"-"+"("+"("+caminos.P([4,1,1])+"O"+caminos.P([4,2,1])+")"+"O"+"("+caminos.P([4,3,1])+"O"+caminos.P([4,4,1])+")"+")"+")"
regla5_t1 = "("+"("+"("+caminos.P([2,0,1])+"O"+caminos.P([2,1,1])+")"+"O"+"("+caminos.P([2,2,1])+"O"+caminos.P([2,3,1])+")"+")"+"O"+"-"+"("+"("+caminos.P([0,1,1])+"O"+caminos.P([1,2,1])+")"+"O"+"("+caminos.P([0,3,1])+"O"+caminos.P([0,4,1])+")"+")"+")"
regla5_b = "("+"("+"("+caminos.P([4,0,0])+"O"+caminos.P([4,1,0])+")"+"O"+"("+caminos.P([4,2,0])+"O"+caminos.P([4,3,0])+")"+")"+"O"+"-"+"("+"("+caminos.P([1,1,0])+"O"+caminos.P([1,2,0])+")"+"O"+"("+caminos.P([1,3,0])+"O"+caminos.P([1,4,0])+")"+")"+")"
regla5_p1 = "("+"("+"("+caminos.P([3,0,0])+"O"+caminos.P([3,1,0])+")"+"O"+"("+caminos.P([3,2,0])+"O"+caminos.P([3,3,0])+")"+")"+"O"+"-"+"("+"("+caminos.P([2,1,0])+"O"+caminos.P([2,2,0])+")"+"O"+"("+caminos.P([2,3,0])+"O"+caminos.P([2,4,0])+")"+")"+")"


q = [regla5_p,regla5_t,regla5_r,regla5_x,regla5_r1,regla5_t1,regla5_b,regla5_p1]
respuesta = Ytoria(q)
print(respuesta)

# ESTAS SON PRUEBAS - - - - - - - - - - - 
#print(regla5_p)
#print(regla5_t)
#print(regla5_r)
#print(regla5_x)
#print(regla5_r1)
#print(regla5_t1)
#print(regla5_b)
#print(regla5_p1)


#print(inorder_to_tree(regla5_p))
#print(inorder_to_tree(regla5_t))
#print(inorder_to_tree(regla5_r))
#print(inorder_to_tree(regla5_x))
#print(inorder_to_tree(regla5_r1))
#print(inorder_to_tree(regla5_t1))
#print(inorder_to_tree(regla5_b))
#print(inorder_to_tree(regla5_p1))