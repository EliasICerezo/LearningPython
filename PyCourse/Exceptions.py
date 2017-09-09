class TestError (Exception):
    def __init__(self,value):
        self.valor=value
    def __str__(self,msg):
        print msg


#Main

raise TypeError("Fallo")


try:
    print 1
except : #ES UN TRYCATCH DE TODA LA VIDA
    print "Ha habido un error de ejecucion"
finally:
    print "executed"
