a=int(input())
values=list(map(int,input().split()))
for i in values:
  if(values.count(i)==1):
    print(i)
    break
