l=[]
i=0

while True:
    if i==25:
        break

    l=l+[i]
    i=i+1

print l


for e in l:
    l[e]=e+1

print l
