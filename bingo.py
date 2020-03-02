import numpy as np
from random import randrange
import collections
import random
l=random.sample(range(1, 100), 25)
matrix = np.array(l).reshape(5,5)

n = input("Enter the number of guesses you want : ") 

l1=[]
print("Enter "+n+" numbers within range 1-100:") 
for i in range(0,int(n)):
    num=int(input("Enter No "+str((i+1))+":"))
    if num>=1 and num<=100:
        l1.append(num)
    else:
        num=int(input("Enter correct number:"))
        if num>=1 and num<=100:
            l1.append(num)

l2=[]
same=[]
sum4=[]

for num in l1:
    if num in matrix:
        result = np.where(matrix == num)
        listOfCoordinates= list(zip(result[0], result[1]))
        #print(result[0])
        if result[0]==result[1]:
            same.append(listOfCoordinates)
        if result[0]+result[1]==4:
            sum4.append(listOfCoordinates)
        
        l2.append(listOfCoordinates)   


l2=list(zip(*l2))

x=[]
y=[]
for i in range(0,len(l2[0])):
    tup=l2[0][i]
    x.append(tup[0])
    y.append(tup[1])

fx=collections.Counter(x)
fy=collections.Counter(y)

l_fx=[]
l_fy=[]
for i in fx.values():
    l_fx.append(i)
        
for i in fy.values():
    l_fy.append(i)
        
if len(same)==5 or len(sum4)==5:
    print("Bingo!!")
elif 5 in l_fx:
    print("Bingo!!")
elif 5 in l_fy:
    print("Bingo!!")
else:
    print("Better luck next time")

print(matrix)




   
