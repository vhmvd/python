from math import inf

def max_val(arr: list) -> int:
  # Negative infinity for smallest number
  max = -inf
  for itr in arr:
    if max < itr:
      # Update max number
      max = itr
      
  return max

def min_val(arr: list) -> int:
  # Positive infinity for largest number
  min = inf
  for itr in arr:
    if min > itr:
      # Update min number
      min = itr
      
  return min

def mean(arr: list) -> float:
  count = 0
  sum = 0
  for itr in arr:
    sum += itr
    count += 1
  return sum/count

def std(arr: list) -> float:
  meann = mean(arr)
  sum = 0
  count = 0
  for itr in arr:
    sum += (itr-meann)**2
    count += 1
  return (sum/count)**0.5

def list_append(arr: list, element: int) -> None:
  arr += [element]

def list_insert(arr: list, location: int, element: int) -> None:
  arr[:location] += [element]
  
def list_add(arr: list, num: int) -> None:
  for itr in range(len(arr)):
    arr[itr] += num

def list_subtract(arr: list, num: int) -> None:
  for itr in range(len(arr)):
    arr[itr] -= num
    
def list_multiply(arr: list, num: int) -> None:
  for itr in range(len(arr)):
    arr[itr] *= num

def list_divide(arr: list, num: int) -> None:
  if num == 0:
    print("Division by 0 not possible")
    return
  for itr in range(len(arr)):
    arr[itr] /= num

def vector_add(arr1: list, arr2: list) -> None:
  if len(arr1) == len(arr2):
    for itr in range(len(arr1)):
      arr1[itr] += arr2[itr]
      arr2[itr] = arr1[itr]


def eleven():
  num = 11
  print("11 x 2  =", num*2)
  print("11 - 7  =", num-2)
  print("11 / 11 =", num/num)
  
def big_list(arr: list, num: int) -> list:
  new_list = []
  for itr in arr:
    if itr > num:
      new_list += [itr]
  return new_list