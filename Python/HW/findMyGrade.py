# get 3 subject input and find the grade
# for any one subject grade 
# A -> 100, B -> range(90to99), C -> range(60to89)
# for all subject grade
# f -> less than 50
# d -> otherwise

# assign function name as findMyGrade() 
# and get subject1, subject2, subject3 as input
def findMyGrade(subject1, subject2, subject3):
    
    # check any one of the subject mark is 100 and then return grade 'A'
    if(subject1==100 or subject2==100 or subject3==100):
        return('A')
        
    # check any one of the subject is the range(90-99) and then return grade 'B'
    if((subject1>=90 and subject1<=99) or (subject2>=90 and subject2<=99) or (subject3<=99 and subject3>=90)):
        return('B')
        
    # check any one of the subject is the range(60-89) and then return grade 'C'
    if((subject1>=60 and subject1<=89) or (subject2>=60 and subject2<=89) or (subject3<=89 and subject3>=60)):
        return('C')
    
    # check all the subject mark is less than 50 and the return grade 'F'
    if(subject1<50 and subject2<50 and subject3<50):
        return('F')
       
    # otherwise return grade 'D' 
    else:
        return('D')
        
# call findMyGrade()
grade = findMyGrade(39,50,49)
print("Your Grade is :", grade)