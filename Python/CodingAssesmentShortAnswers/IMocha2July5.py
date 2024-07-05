""" i=3.2
x=float(i)==int(i)
print(x)
j=3
y=float(j)==int(j)
print(y) """

my_list=[3,1,8,9]

while (float(sum(my_list)/len(my_list))!=int(sum(my_list)/len(my_list))):
       my_list[0]=my_list[0]+1
print(sum(my_list))