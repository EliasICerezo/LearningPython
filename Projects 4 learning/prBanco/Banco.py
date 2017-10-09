import Cuenta

class banco:
    def __init__(self,nb):
        self.__maxCntas=10
        self.nombre=nb
        self.cuentas={}
        self.ppl=0
        self.unca=1001

    def abrirCuenta(self,nb,saldo):
        if saldo is None:
            c=Cuenta.Cuenta(nb,self.unca,0.0)
        else :
            c=Cuenta.Cuenta(nb,self.unca,saldo)

        self.cuentas[self.unca]=c
        self.unca+=1

    def cerrarCuenta(self,num):
        self.cuentas.pop(num)

    def ingreso(self,num,saldo):
        c=self.cuentas.get(num,0)
        if c==0:
            raise Exception("No se encontro la cuenta")
        c.ingreso(saldo)
        self.cuentas[num]=c

    def debito(self,num,sal):
        c = self.cuentas.get(num, 0)
        if c == 0:
            raise Exception("No se encontro la cuenta")

        c.debito(sal)
        self.cuentas[num]=c
        return sal

    def transferencia(self,na,nb,saldo):
        c1=self.cuentas.get(na,0)
        c2=self.cuentas.get(nb,0)
        if c1==0 or c2==0:
            raise Exception("Error los indices no son validos")

        c2.ingreso(c1.debito(saldo))
        self.cuentas[na]=c1
        self.cuentas[nb]=c2



def printCuentas(b):
    print("\n")
    for e in b.cuentas.values():
        print(e.toString())
        print("\n")


#Main


b=banco("España")

print (b.nombre)

b.abrirCuenta("Elias",1000.0)
b.abrirCuenta("Juanjo",100.0)
b.abrirCuenta("Dani", 700.0)
print (b.cuentas)

b.cerrarCuenta(1001)

print (b.cuentas)

b.ingreso(1003,1000.0)

printCuentas(b)

b.ingreso(1002,1500.0)

printCuentas(b)

b.debito(1003,500.0)

printCuentas(b)

b.transferencia(1002,1003,3000.0)

printCuentas(b)