def operador(n,m):
    if n==None or m==None:
        return 0
    else:
        return n+m

def aux(a):
    return a**2+a*3+a+7


l1=[1,2,3,4]
t1= 9,8,7,6

print map(operador,l1,t1)

#EXACTAMENTE IGUAL QUE HASKELL
