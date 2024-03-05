# open and read the 'file.txt'
# find the 4 letter words and count the word

passage = open("./day3/file.txt",'r')
passage = passage.read().replace('.','').lower()
passage = passage.split()

# assign empty list for store the 4 letter words
a = []

# strore the 4 letter words in list a[]
for i in passage:
    if len(i)==4:
        a.append(i)

# store the unique words in set 'b'
b=set(a)

# count the no of times the unique word occurred
for i in b:
    # initialy count 0 ( for every idretion it's make 0 )
    count = 0
    for j in range(len(a)):
        if a[j]==i:
            # increment the count value
            count+=1
    # print the unique word and it's count
    print(i,":",count)
