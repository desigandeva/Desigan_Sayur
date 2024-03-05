# add the previus character in front and end of the next character until 'g'
# ord() is an in-buid function to convert character to decimal value
# chr() is convert decimal value to character


# assign empty character as 'c'
c = ''
# for loop at a range of (0-7) because until we use 'g'
for i in range(0,7):
    # add previous charater in front and end of this current character
    c=c+chr(ord('a')+i)+c
    # print the character
    print(c)