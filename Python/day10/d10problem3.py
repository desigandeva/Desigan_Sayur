# Add two number represented in a list as reversed
# print the sum also as a list in reverse order

# list1
list1 = [1,2,3]
# list2
list2 = [5,6,7]
# empty string
a=''
b=''
# revers the list1 and convet to string
for i in list1[::-1]:
    a=a+str(i)

for i in list2[::-1]:
    b=b+str(i)

# add a and b
sum = int(a)+int(b)
# print the sum
print(sum)