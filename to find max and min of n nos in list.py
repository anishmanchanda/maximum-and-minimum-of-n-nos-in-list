#to find maximum and minimum number from a list

n=int(input("enter number of numbers"))
max=-99999999
min=99999999
list=[]
for i in range (n):
    num = int(input("enter a number"))
    list.append(num)

    if num>=max:
        max=num
       
    if num<=min:
        min=num
        
print(list)        
print("largest of the list is",max)
print("smallest of the list is",min)
