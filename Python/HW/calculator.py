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

user_input = input("Enter your equation : ")
basicCal(user_input)
