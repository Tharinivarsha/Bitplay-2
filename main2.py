#Activity2
def Oddoccuringnumbers(arr):
    res=1
    for element in arr:
     res=res ^ element
    return res
arr=[]
n=int(input("Enter the array size: "))
while(n):
    number=int(input("Enter the number: "))
    arr.append(number)
    n-=1
print("Odd occuring number is: ",Oddoccuringnumbers(arr))