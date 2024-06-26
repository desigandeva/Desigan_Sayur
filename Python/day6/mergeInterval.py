# Program 2
# Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
# For example, 
# Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
# Output [[1,6],[8,10],[15,25]].
# 
# Given a collection of two numbers that specify an interval, 
# merge all overlapping intervals. 
# get list of intervals
# 


# input list
in_list = [[1,3],[2,6],[8,10],[15,20],[16,25]]

# build a function for merge overlapped intervals
def mergeInterval(input_list):
    # output list
    out_list = []
    # initialize item as 0
    item=0
    while item< len(input_list):
        # temp empty list
        temp_list = []
        if item<len(input_list)-1:
            # find overlapped interval and rearrange
            if input_list[item][1]>input_list[item+1][0]:
                # add starting interval to temp_list
                temp_list.append(input_list[item][0])
                # add ending interval to temp_list
                temp_list.append(input_list[item+1][1])
                # add temp_list to out_list
                out_list.append(temp_list)
                # increment item by 1
                item+=1
            # do nothing
            else:
                # add starting interval to temp_list
                temp_list.append(input_list[item][0])
                # add ending interval to temp_list
                temp_list.append(input_list[item][1])
                # add temp_list to out_list
                out_list.append(temp_list)
        # increment item by 1
        item+=1
    # return perfect interval
    return out_list

# call mergeInterval() fumction and print output
print(mergeInterval(in_list))
