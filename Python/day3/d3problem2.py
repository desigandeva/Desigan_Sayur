# read the passage from file
# import os
# print(os.getcwd())
# open and read file 
passage = open("./day3/file.txt","r")
passage = passage.read().replace('.','').lower()
passage = passage.split()

count = 0
status = False
print(passage)
# print(passage.)
for i in range(len(passage)):
    if passage[i]=='a':
        status=not(status)
        print(status)
    if passage[i]=="the" and status==False:
        count+=1
    if passage[i]=='the' and status==True:
        count=count
    
print(count) 