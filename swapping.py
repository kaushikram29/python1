x=str(input())
y=list(x)
y[::2],y[1::2] =y[1::2],y[::2]
print (''.join(y))
