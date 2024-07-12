def HIndex(list):
    index = 0
    while True:
        count = 0
        for paper in list:
            if paper >= index:
                count += 1
                if count >= index:
                    break

        if count >= index:
            index += 1
        else:
            return index - 1  #this is the first index that is too high so have to subtract 1


#Example 1:
#Input: 
citations = [3,0,6,1,5]
print(HIndex(citations))
#Output: 3
#Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
#Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

#Example 2:
#Input: 
citations = [1,3,1]
print(HIndex(citations))
#Output: 1
 