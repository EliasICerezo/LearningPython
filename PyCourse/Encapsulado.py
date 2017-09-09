class Prueba(object):
    def __init__(self):
        self.__privado = "PRIVATE"
        self.publico = "PUBLIC"

    def __metodoP(self):
        print "Soy priv"

    def metodopublico(self):
        print "Soy public"

    def getPriv(self):
        return self.__privado

    def setPriv(self,value):
        self.__privado=value
#Main
obj= Prueba()

#print obj.privado
#print obj.__privado

obj.metodopublico()
#obj.__metodoP()

print obj.getPriv()

obj.setPriv("YOLOOOOOOOOOO")

print obj.getPriv()
