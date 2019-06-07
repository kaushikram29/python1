a=int(input())
R=0
while(a>0):
  n=int(a%10)
  R = int((R*10) +(n))
  a = int(a/10)
print (R)
