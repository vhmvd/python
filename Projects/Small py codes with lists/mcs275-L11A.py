def merge(L, R):
    """
    Returns the merger of lists L and R,
    appending minimum(L[0], R[0]) to M every time.
    """
    M = []
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            M.append(L.pop(0))
        else:
            M.append(R.pop(0))
    if len(L) > 0: # this picks up the last remaining element in L if it exists
       return M + L
    else:
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
     print(recursive_merge_sort([4,1,7,2,8,6,3]))
main()
