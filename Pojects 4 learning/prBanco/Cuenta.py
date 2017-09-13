class Cuenta:

    def __init__(self,tit,num,sal):
        self.numero=num
        self.titular=tit
        if sal<0:
            self.saldo=0
        else:
            self.saldo=sal

    def ingreso(self,s):
        self.saldo+=s

    def debito(self,s):
        if s>self.saldo:
            ret=self.saldo
            self.saldo=0
            return ret
        else:
            self.saldo-=s
            return s

    def toString(self):
        s="Titular: "+str (self.titular)+"\nNumero: "+str(self.numero)+"\nSaldo: "+str(self.saldo)
        return s


#MAIN

#cu=Cuenta("Elias",0,10.0)

#print (cu.toString())

#cu.ingreso(10.0);
#cu.ingreso(5.0)
#cu.debito(3.0)
#print("\n")
#print (cu.toString())

