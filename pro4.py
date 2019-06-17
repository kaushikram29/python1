s1,s2=input().split()
T=0
if len(s1)>len(s2):
  s1,s2=s2,s1
j=0
while j<len(s1):
  T+=(ord(s2[j])-ord(s1[j]))
  j+=1
for j in range(j,len(s2)):
  t+=ord(s2[j])-ord('a')+1
print(T)
