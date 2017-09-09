#PARTE DE PROG FUNCIONAL
#Podemos definir funcioines sin tener necesariamente una clase de por medio
#Esto, entre otras cosas lo que nos permite es hacer programacion funcional con el lenguaje

def test(f):
    return f()

def aux():
    return 2+2

#SPARSEVECTORS EN PYTHON PROXIMAMENTE


#MAIN
print test(aux)
