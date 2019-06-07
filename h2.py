a=int(input())
g=list(map(int,input().split()))
g.sort(reverse=True)
for m in range(0,a):
  print(g[m],end="")
