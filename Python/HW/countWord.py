# list = [good,god,good,abc,cba,aaa,ccc,good]
# (dgo->good,god,good,good) and (abc->abc,cba)
# count - 2 
# list = [good,good]
# (dgo->good,good)
# count - 1
# list = [abc,bac,good]
# (abc->abc,bac)
# count - 1
# list = [deer,red,god,dog,abc,bca]
# (der->deer,red) and (dgo->god,dog) and (abc->abc,bca)
# count - 3
# 
# 

# build a function for remove duplicate character in given word
def removeDupCharInWord(word):
    # temp word
    temp = ''
    for char in word:
        if char not in temp:
            # add unique character in temp
            temp += char
    # return sorted temp word
    return ''.join(sorted(temp))

# build a function for find same character word in given list and count of them
def findSameCharWords(word_list1):
    # make empty dictionary as count_dic
    count_dic = {}
    # word_list2 to store the removed duplicate character words
    word_list2 = []
    # get word from list_of_words
    for word in word_list1:
        # call removeDupCharInWord() function it's return duplicate removed string in ascending order
        word_list2.append(removeDupCharInWord(word))
    # loop until the word in word_list2    
    for index in range(len(word_list2)):
        # check the string not in count_dic
        if word_list2[index] not in count_dic:
            # add the word to the count_dictionary
            count_dic[word_list2[index]] = {"word" :word_list1[index],"count" : 1}
        else:
            # add the word to the count_dictionary
            count_dic[word_list2[index]]["word"] += ','+word_list1[index]
            # increment the count
            count_dic[word_list2[index]]["count"] += 1
    # return the count_dic
    return count_dic


# build countSameCharWords() function for count the same character word in given list
def countSameCharWords(list_of_words):
    # new_list to store the removed duplicate character words
    new_list = []
    # sorted_list to store the unique strings
    sorted_list = []
    # initialize count as 0
    count = 0
    # get word from list_of_words
    for word in list_of_words:
        # call removeDupCharInWord() function it's return duplicate removed string in ascending order
        new_list.append(removeDupCharInWord(word))
    # get unique string from new_list and stored in sorted_list
    sorted_list = list(set(new_list))
    # get word from sorted_list
    for word in sorted_list:
        # count the word in new_list,and check count >= 2
        if new_list.count(word) >= 2:
            # increment count by 1
            count+=1
    # return the count
    return count

# main function
def main():
    try:
        # input_list
        # input_list = ['good','god','gode','abc','bca','aaa','ccc','dog','cab','good','gdeo']
        input_list = input("Enter word's (seperated by ,) : ").split(',')

        # print input_list
        print('\nGiven List :',input_list,'\n')

        # call countSameCharWords(list)
        print("Count :",countSameCharWords(input_list),'\n')

        # call the findSameCharWordsAndCount(list)
        word_dic = findSameCharWords(input_list)

        # initialize count as 0
        count = 0
        # get key, value form word_dic
        for key, value in word_dic.items():
            # chech the count > 2
            if word_dic[key]["count"]>=2:
                # increment the count by 1
                count += 1
                # print the character's and word's
                print("Character's :",key,"  Word's :",word_dic[key]["word"])
        
        # print the count
        print("Count :",count,'\n')

    except Exception as e:
        print(e)

    # return 0
    return 0

# call main() function
main()