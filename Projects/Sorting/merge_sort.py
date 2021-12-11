import random

def generator(size: int) -> list:
  """Genrates the list in given size

  Args:
      size (int): Size of the list required

  Returns:
      list: Random ints list
  """
  numbers_list = []
  for _ in range(random.randint(0, size)):
    numbers_list.append(random.randint(0, size))
  return numbers_list

def in_thousand_range() -> list:
  return generator(1000)
  
def in_million_range() -> list:
  return generator(1000000)
  
def in_billion_range() -> list:
  return generator(1000000000)


def merge_lists(left_list, right_right):
  i = 0
  j = 0
  result = []
  while i<len(left_list) and j<len(right_right):
    if left_list[i] <= right_right[j]:
      result.append(left_list[i])
      i += 1
    else:
      result.append(right_right[j])
      j += 1
  result += left_list[i:]
  result += right_right[j:]
  return result

def merge_sort(numbers_list):
  if len(numbers_list) <= 1:
    return numbers_list
  else:
    mid = int(len(numbers_list)/2)
    left = merge_sort(numbers_list[:mid])
    right = merge_sort(numbers_list[mid:])
    return merge_lists(left,right)


number_list = in_thousand_range()
sorted_list = merge_sort(number_list)
with open('merge_thousand.txt', 'w') as fd:
  for number in sorted_list:
    fd.write(str(number)+"\n")
number_list.clear()
sorted_list.clear()

number_list = in_million_range()
sorted_list = merge_sort(number_list)
with open('merge_million.txt', 'w') as fd:
  for number in sorted_list:
    fd.write(str(number)+"\n")
number_list.clear()
sorted_list.clear()

number_list = in_billion_range()
sorted_list = merge_sort(number_list)
with open('merge_billion.txt', 'w') as fd:
  for number in sorted_list:
    fd.write(str(number)+"\n")
number_list.clear()
sorted_list.clear()