A = int(input())
B = int(input())
for i in range(A, B + 1):
   O = len(str(i))
   sum = 0
   temp = i
   while temp > 0:
       digit = temp % 10
       sum += digit ** O
       temp //= 10
       if i == sum:
          print(i)
