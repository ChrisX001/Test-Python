x = int(input("enter a number "))
def fibo(x):
    if x == 1 or x == 2:
        return 1
    elif x>2:
        return fibo(x-1)+fibo(x-2)
    elif x<1:
        return -1
p = (fibo(x))
print (p)
k = 0
c = True
for i in range(0,20,1):
    if ((i ** p) % p == (i % p)):
        k = k
    else:
        k = k + 1
if k == 0 :
    print ("o arithmos einai prwtos")
else :
    print ("o arithmos den einai prwtos")