# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# 
# look at the output and find the pattern. Hint - add next letter in the alphabet in each row
# 
# add the previus character in front and end of the next character until 'g'
# ord() is an in-buid function to convert character to decimal value
# chr() is convert decimal value to character
# 

# assign empty character as 'chracter'
chracter = ''
# for loop at a range of (0-7) because until we use 'g'
for num in range(0,7):
    # add previous charater in front and end of this current character
    chracter=chracter+chr(ord('a')+num)+chracter
    # print the character
    print(chracter)
