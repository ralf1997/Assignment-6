#Q1

PI = 3.14
radius = float(input('Please Enter the Radius of a Sphere: '))
sa =  4 * PI * radius * radius
print("\n The Surface area of a Sphere = %.2f" %sa)

#Q2

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

#Q3

n = int(input("Input a number: "))

for i in range(1,11):
   print(n,'x',i,'=',n*i)

#Q4

def rpower(num,idx):
    if(idx==1):
       return(num)
    else:
       return(num*rpower(num,idx-1))
base=int(input("Enter number: "))
exp=int(input("Enter index: "))
rpow=rpower(base,exp)
print("{} raised to {}: {}".format(base,exp,rpow))
