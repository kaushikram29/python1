a=int(input())
h=[]
for l in range(0,a):  
    d=input()
    h.append(d)
list=[]
for l in zip(*h):
    if (l.count(l[0])==len(l)): 
        list.append(l[0])
    else:
        break
print(''.join(list))
