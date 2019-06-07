a=int(input())
b=input().split()
k=[]
for i in range(0,a):
  if(int(b[i])==i):
    k.append(b[i])
if(k==[]):
  print("-1")
else:
  k.sort()
  for j in range(0,len(k)):
    print(k[j],end=" ")
