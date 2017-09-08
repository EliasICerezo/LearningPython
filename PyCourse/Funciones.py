
def fn (l=[],*extras): # con un * = tupla con **= diccionario, para ese diccionarui tenemos que poner una asignacion, el lado izquierdo sera la clave del diccionario y el derecho sera el value del mismo.
    res=0;
    for i in l:
        res=res+l[i]
    return res


l=[]
j=0
while True:
    if j==5:
        break

    l=l+[j]
    j=j+1

print l
print fn(l)
