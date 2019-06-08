a,b=map(int,input().split())
k=list(map(int,input().split()))
result=1
for i in range(0,len(k)):
	for j in range(i+1,len(k)):
		m=k[i]+k[j]
		if m==b:
			result=0
if result==0:
	print("yes")
else:
	print("no")
