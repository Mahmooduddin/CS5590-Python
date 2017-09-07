list=[] # define list
for i in range(700,1700): # iterate between 700 to 1700
   if (i%5==0) and (i%2==0): # if number is divisible by 5 and multiple of 2
     list.append(str(i)) # append the number in the string
print(','.join(list))   # join numbers in the list seperated with coma and print