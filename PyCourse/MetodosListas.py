lista = [1,2,3,4,5,6]

buscar= 0

if buscar in lista: #In es como elem en haskell
    print lista.index(buscar) # Como si fuera indexof en java
else:
    print "El elemento no se encuentra en la lista"

lista.append(0)
lista.append(0)

print lista

print "El elemento que buscas se encuenta "+str(lista.count(0)) + " veces en la lista"

lista.insert(1,2)

print lista

iterable=(7,8,9,0)
lista.extend(iterable)
print lista

print lista.pop(0)

print lista

lista.sort() #OP

print lista

lista.remove(0)
lista.remove(5)

print lista
