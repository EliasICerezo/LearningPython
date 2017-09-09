def decorador(fn):
    def fndecorada(*args,**kwargs):
        fn(*args,**kwargs)

    return fndecorada

@decorador
def resta(n,m):
    print n-m



#Decorado
resta(5,3)
