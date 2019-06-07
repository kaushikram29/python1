A,B=input().split()
X=0
if len(A)!=len(B):
    print("no")
else:
    for i in range(len(A)):
        if A[i]!=B[i]:
            X+=1
if X==1:
    print("yes")
else:
    print("no")
