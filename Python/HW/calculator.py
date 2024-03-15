# build a calculator program


def basicCal(user_input):
    print()
    if '+' in user_input:
        user_input = user_input.split('+')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 + val2
        print("Result : ",val1,'+',val2,'=',result)
    elif '-' in user_input:
        user_input = user_input.split('-')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 - val2
        print("Result : ",val1,'-',val2,'=',result)
    elif '*' in user_input:
        user_input = user_input.split('*')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 * val2
        print("Result : ",val1,'*',val2,'=',result)
    elif '/' in user_input:
        user_input = user_input.split('/')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 / val2
        print("Result : ",val1,'/',val2,'=',result)
    elif '%' in user_input:
        user_input = user_input.split('%')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 % val2
        print("Result : ",val1,'%',val2,'=',result)
    elif '//' in user_input:
        user_input = user_input.split('//')
        val1 = int(user_input[0])
        val2 = int(user_input[1])
        result = val1 // val2
        print("Result : ",val1,'//',val2,'=',result)
    return 0

eq_list = []
def splitEquation(user_input):
    if user_input:
        global eq_list
        for i in range(len(user_input)):
            if user_input[i]=='+' or user_input[i]=='-' or user_input[i]=='/' or user_input[i]=='*':
                eq_list.append(user_input[:i])
                eq_list.append(user_input[i])
                user_input = user_input.replace(user_input[:i+1],'')
                return splitEquation(user_input)
        if ('+' not in user_input) and ('*' not in user_input) and ('/' not in user_input)and ('-' not in user_input):
            eq_list.append(user_input)
            return 0

def calculator(user_input):
    result = int(user_input[0])
    index = 1
    while index<len(user_input):
        if user_input[index]=='+':
            print(result,'+',user_input[index+1])
            result += int(user_input[index+1])
            index+=1
        elif user_input[index]=='-':
            print(result,'-',user_input[index+1])
            result -= int(user_input[index+1])
            index+=1
        elif user_input[index]=='*':
            print(result,'*',user_input[index+1])
            result *= int(user_input[index+1])
            index+=1
        elif user_input[index]=='/':
            print(result,'/',user_input[index+1])
            result /= int(user_input[index+1])
            index+=1
        index+=1
    return result

user_input = input("Enter your equation (seperate by space) : ")
# basicCal(user_input)
splitEquation(user_input)
print("Final Result : ",calculator(eq_list))


