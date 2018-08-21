# q.1- Reverse the list.

n=int(input("Enter the number of elements"))
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
print(l)
l.reverse()
print(l)

# q.2- Extract all the uppercase letters from a string.

print("Enter string")
s=input()
st=""
for a in s:
    if(a.isupper()==True):
        st=st +a
print(st)

# q.3- Split and store the values after typecasting

p=input("Enter Values").split(",")
l2=[]
for i in p:
    l2.append(int(i))
print(l2)

# q.4- Check for palindrome.

print("Enter a string")
strr=input()
r="".join(reversed(strr))
print(strr,r)
if(strr==r):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
    
# Q.5- Understand Deep and Shallow Copy

# DeepCopy
import copy as c
l3=[1,2,3,[9,5]22,20,8]
l4=c.deepcopy(l3)
print(l3)
print(l4)
l4[3][1]=15
print(l3)
print(l4)   #only l4 is updated


# ShallowCopy
import copy as c
l5=[1,2,3,[9,5],22,20,8]
l6=l5.copy(l5)
print(l5)
print(l6)
l6[3][1]=13
l6[3][0]=17
print(l1)
print(l2)   #there is changes in both list

#DIFFERENCE
'''
Difference between Shallow copy and Deep copy is that
in shallow copy if the original object contain any references
to mutable object then the duplicate
reference variable will be created pointing to the
old object and no duplicate object is created whereas
in deep copy a duplicate object is created.
'''
