"""
All variables declared outside of functions are global. Variables declared inside functions are local. In Python, the keyword "global" allows us to modify a global variable in a local context.
We will use it here as a tool to solve the line intersection count problem - using a slightly modified version of the recursive merge sort function. The use of a global variable here provides a bit of an alternative to the memoization process we covered few lectures ago.   
"""
K = 0 # here we declare a variable, and initialize it to zero.

def recursive_merge_sort(data):
    """
    This function is a modified version of the merge sort functions from 
    Lecture 11, written here as a single function.
    Here we illustarte the use of a global variable, modified within a local context. 
    """

    global K # a reference to the variable K, declared outside of this function.  
 
    if len(data) <= 1:
       return data
    else:
        middle = (len(data)+1)//2 
        L = recursive_merge_sort(data[:middle])
        R = recursive_merge_sort(data[middle:])
        
        M = []
        while len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
               M.append(L.pop(0))
            else:
               M.append(R.pop(0))
               K += len(L)   # here we count the number of inversion
        if len(L) > 0:
           return M + L
        else:
           return M + R


print(recursive_merge_sort([4,3,7,6,5,2,4,1,0,7]))
print("the number of line intersections = ", K)

