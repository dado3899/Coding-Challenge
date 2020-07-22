def SummationinList(List, Sum):
    #Create Empty List
    PreviousNums = []
    #Iterate through listofnumbers
    for i in List:
        #If the i plus a previous number is equivilent to Sum then return True (meaning Sum-i should exist in the previous numbers List
        if Sum-i in List:
            print(i, "+", Sum-i,"=",Sum)
            return True
        #Otherwise add current number to previous numbers and continue
        else:
            PreviousNums.append(i)
    #If the for list returns nothing that means there is no sum of values
    print("No Sum in given list is", Sum)
    return False

#Test function
ListOfNumbers = [1, 8, 5, 12]
Target = 20
SummationinList(ListOfNumbers, Target)