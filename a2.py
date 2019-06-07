a=input()
a=int(a)
x1=[]
for j in range(0,a):  
    N1=input()
    z1.append(N1)
g1=[]
for j in zip(*x1):
    if j.count(j[0])==len(j): 
        g1.append(j[0])
    else:
        break
print(''.join(g1))
