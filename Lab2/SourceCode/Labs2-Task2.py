#ask user to enter any number
n=int(input("give any number: "))
#define dictionary
a=dict()
#use for loop
for i in range(1,n+1):
    a[i]=i*i
#print a
print(a)