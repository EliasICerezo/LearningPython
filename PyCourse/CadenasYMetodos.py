s="Hola Mundo"
t=("Hola","Mundo")
r=" "
print "Length: "+str(len(s))

print  "Numero de veces que aparece o: " + str(s.count('o'))

print s.lower()

print s.upper()

print s.replace("o","x") # Como parametro opcional se puede anyaddir cuantas coincidencias quieres reemplazar

print s.split(" ")

print "EL caracter buscado esta en la posicion: "+str(s.find("a"))

print r.join(t)
