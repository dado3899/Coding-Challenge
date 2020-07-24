def LowestPosInt(IntList):
    #Give the lowest possible positive int
    Lowest=1
    #Sort the List
    SortedList = sorted(IntList)
    #For every value in the sorted list, if it is equivilent to the lowest value that means that the lowest value exist, so we should bump up the lowest value by 1
    for i in SortedList:
        if i == Lowest:
            Lowest=Lowest+1
    return Lowest

List = [5,3,4,9,2,1,-1,5,2]
List2 = [1, 2, 0]
print(LowestPosInt(List))
print(LowestPosInt(List2))