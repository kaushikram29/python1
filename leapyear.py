y=int(input("Enter year to be checked:"))
if(y%100!=0 and y%4==0 or year%400==0):
    print("The year",y," is a leap year")
else:
    print("The year",y," isn't a leap year!")
