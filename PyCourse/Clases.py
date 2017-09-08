class Jarra:

    def __init__(self,cap):
        self.capacidad=cap
        self.contenido=0

    def llena(self):
        self.contenido=self.capacidad

    def vacia(self):
        self.contenido=0

    def capacidad(self):
        return self.capacidad

    def contenido(self):
        return self.contenido

    def vaciaen(self,Jarra):
        if(Jarra.capacidad-Jarra.contenido>=self.capacidad):
            Jarra.contenido= self.contenido
            self.contenido=0
        else:
            self.contenido=self.contenido-(Jarra.capacidad-Jarra.contenido)
            Jarra.contenido=Jarra.capacidad

class JarraCristal(Jarra):
    def romperse(self):
        print 'La jarra se ha roto'


#Main
j=Jarra(7)
j2=Jarra(5)
j3= JarraCristal(5)

print 'J3CAP: ' + str(j3.capacidad)
print 'J3CONT: ' + str(j3.contenido)



j.llena()

j.vaciaen(j2)

print 'J1: '+ str(j.contenido)
print 'J2: '+ str(j2.contenido)
