N = 371
S = 0
T = N
while T > 0:
   D = T % 10
   S += D ** 3
   T //= 10
if N == S:
   print("yes")
else:
   print("no")
