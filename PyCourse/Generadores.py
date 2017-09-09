
def gennum(n):
    i=0
    while n>0:
        yield i
        i+=1
        n-=1


#Main
j=20
for e in gennum(20):
    print e
