def quick_sort(data):
    """
    INPUT: data, a list of integers to be sorted
    OUTPUT: sorted list in ascending order
    """
    if len(data) <= 1:
        return data
    else:
        S = [] # smaller than pivot values 
        G = [] # greater than pivot values
        pivot = data[0]
        for value in data[1:]:
            if value < pivot:
                S.append(value)
            else:
                G.append(value)
        #concatination of 3 lists, with pivot in the middle
        #since pivot is an int, we put it inside a list and concatinate
        #think of Python strings as an analogy
        return quick_sort(S)+[pivot]+quick_sort(G)

def main():
    print(quick_sort([6,9,4,2,7,1,8,0,3]))
main()
