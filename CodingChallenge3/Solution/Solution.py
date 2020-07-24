#Given class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Serialize(node):
    #Recursive Function that repeats itself adding each value to the string
    def Serialize2(node, str=[]):
        if node:
            str.append(node.val)
            str=Serialize2(node.left,str)
            str=Serialize2(node.right,str)
        else:
            str.append('NA')
        return str
    SerStr = Serialize2(node)
    #Turn List to string as it wants a string as a return, split by spaces
    return ' '.join(SerStr)

# I had to look up the method as my original one had some weird errors, It took this base logic but the issue came with how I did SerStr, I did not use an iter to make it easy to carry each value
# so my method was dirty and did not work. An odd issue was that no matter what I did, adding my .split of SerStr did not work within the function and I could only solve it by moving it outside.
def Deserialize(SerStr):
    def Deserialize2(iterlist):
        val=next(iterlist)
        if val == 'NA':
            return None
        TMPNode = Node(val)
        TMPNode.left = Deserialize(iterlist)
        TMPNode.right = Deserialize(iterlist)
        return TMPNode
    vals= iter(SerStr)
    return Deserialize2(vals)

node = Node('root', Node('left', Node('left.left')), Node('right'))
SerStr = Serialize(node)
Test = SerStr.split()
print(Deserialize(Test).left.left.val)