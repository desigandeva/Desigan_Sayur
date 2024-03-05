# Given a collection of two numbers that specify an interval, 
# merge all overlapping intervals. 
# get list of intervals

# input list
in_list = [[1,3],[2,6],[8,10],[15,20],[16,25]]

# build a function for merge overlapped intervals
def mergeInterval(lst):
    # output list
    out_list = []
    i=0
    while i< len(lst):
        # temp empty list
        temp = []
        if i<len(lst)-1:
            # find overlapped interval and rearrange
            if lst[i][1]>lst[i+1][0]:
                temp.append(lst[i][0])
                temp.append(lst[i+1][1])
                out_list.append(temp)
                i+=1
            # do nothing
            else:
                temp.append(lst[i][0])
                temp.append(lst[i][1])
                out_list.append(temp)
        i+=1
    # return perfect interval
    return out_list

# call mergeInterval() fumction and print output
print(mergeInterval(in_list))
