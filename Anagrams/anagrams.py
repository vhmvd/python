def user_interface(dict_obj):
  """Creates the CLI menu to check against a work if anagrams exist

  Args:
      dict_obj (Dict): Contains sorted words as a keys and words in a list
  """
  while True: #Runs until the word is empty input
    word = input("Enter a word (press enter to exit)> ")
    if word == "":
      return
    sorted_word = sorted(word)
    sorted_data_word = ""
    for char in sorted_word:
      sorted_data_word += char
    if sorted_data_word in dict_obj:
      anagrams = dict_obj[sorted_data_word]
      output = ""
      for itr in anagrams:
        output += itr+" "
      print("Anagrams of " + word + ":", output)

def create_dictionary(file):
  """Takes the file handle and generates the dictionary

  Args:
      file (File_handle)
  """
  anagrams_dict = dict()
  for data in file:
    sorted_data = sorted(data)  #Sorts the word to act as a key as anagrams have same chars
    sorted_data_word = ""
    for char in sorted_data:    #Sorted function creates a sorted list so turning it back to a string
      sorted_data_word += char
    if sorted_data_word in anagrams_dict:   #If the key exists appends the word in the value (list)
      anagrams_dict[sorted_data_word].append(data)
    else: #If key does not exits creates a new key/value pair. Here value is a list
      anagrams_dict[sorted_data_word] = [data]
  user_interface(anagrams_dict)
  return

def read_file(file_name):
  """Receives the file name and checks if the file exists or throws an error

  Args:
      file_name (String): file name or path
  """
  try:
    file_handle = open(file_name, "r")     #opens the file
    file = file_handle.read().splitlines() #removes \n from the files and creates a list
    create_dictionary(file)
  except:
    print("Wrong file name or path")



read_file("alphabet.txt")