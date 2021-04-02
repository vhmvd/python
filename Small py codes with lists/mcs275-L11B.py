# Merging process illustration, using a global variable

"""
All variables declared outside of functions are global. Variables declared inside functions are local. In Python, the keyword "global" allows us to modify a global variable in a local context.
We will use it here as a tool to solve the line intersection count problem - using a slightly modified version of the recursive merge sort function. The use of a global variable here provides a bit of an alternative to the memoization process we covered few lectures ago.   
"""
X = [] # here we declare a list variable. we will use it as our global variable

def merge(L, R):
    """
    Returns the merger of lists L and R,
    appending minimum(L[0], R[0]) to M every time.
    """
    global X # declaring X, defined outside, as our global variable 
    M = []
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            M.append(L.pop(0))
        else:
            M.append(R.pop(0))
    if len(L) > 0: # this picks up the last remaining element in L if it exists
       X.append(M+L)
       return M + L
    else:
       X.append(M+R)
       return M + R

def recursive_merge_sort(data):
    """
    Returns a list with the data
    sorted in increasing order.
    """
    if len(data) <= 1:
        return data
    else:
        middle = (len(data)+1)//2 #keeps just the integer component on division, we add 1 to make left side larger
        left = recursive_merge_sort(data[:middle])
        right = recursive_merge_sort(data[middle:])
        return merge(left, right)

def main():
     #print(recursive_merge_sort([5,2,8,3,9,7,4,1]))
     print(recursive_merge_sort([4,3,7,6,5,2,4,1,0,7]))
     print("Merge inclusion order: ", X)
main()
