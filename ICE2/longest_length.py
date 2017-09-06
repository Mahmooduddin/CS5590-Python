list = ["PHP", "Exercises", "Backend"]
my_list=[]
for i in list:
    t=(len(i),i)
    my_list.append(t)
    print(my_list)
my_list.sort()
print((my_list[-1][1]))
