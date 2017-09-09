
diccionario= {
    "ADA" : 6,
    "ED" : 8,
    "INTSYS":10,
}

print diccionario.has_key("ADA")

print diccionario.items() #Keysvalues

print diccionario.keys()

print diccionario.values()

print diccionario.pop("ADA","Vacio")

print diccionario

diccionario["EC"] = 9

print diccionario

d=diccionario.copy()
