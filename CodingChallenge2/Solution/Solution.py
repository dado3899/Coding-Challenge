#This code finds the product of the list, then goes through and divides by each element of the list giving you the product of everything but j in this case
def productbutone(Original):
    #initialize
    ProdList = []
    product = 1
    #Find product of list
    for i in Original:
        product = i * product
    #Divide by each element and appends
    for j in Original:
        ProdList.append(product/j)
    print(ProdList)
    return ProdList
#This one would be if you can't use division, in which it has a nested for loop in which it keeps track of the position i is in, and multiplies every element but the element that is at position i
def productbutoneNoDiv(Original):
    #initialize
    ProdList = []
    #Goes through each number
    for i in range(len(Original)):
        Product = 1
        #Calculates the product of every number excluding the number youy are on (i) and appends
        for j in range(len(Original)):
            if j != i:
                Product = Product * Original[j]
        ProdList.append(Product)
    print(ProdList)
    return ProdList


Original = [1,2,3,4,5] 
productbutone(Original)
productbutoneNoDiv(Original)