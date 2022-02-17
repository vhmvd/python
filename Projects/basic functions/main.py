import func

if __name__ == "__main__":
  A = [12,334,-64,-32,13,-234]
  B = [-12,-334,64,32,-13,234]
  print("List:", A)
  print("Max:", func.max_val(A))
  print()
  
  print("List:", A)
  print("Min:", func.min_val(A))
  print()
  
  print("List:", A)
  print("Mean:", func.mean(A))
  print()
  
  print("List:", A)
  print("Std. Deviation:", func.std(A))
  print()
  
  print("List:", B)
  func.list_append(B, 2)
  print("Append (2):", B)
  print()
  
  print("List:", B)
  func.list_insert(B, 2, 23)
  print("Insert (23) at (2):", B)
  print()
  
  print("List:", B)
  func.list_add(B, 1)
  print("Add (1):", B)
  print()
  
  print("List:", B)
  func.list_subtract(B, 3)
  print("Subtract (3):", B)
  print()
  
  print("List:", B)
  func.list_multiply(B, 4)
  print("Multiply (4):", B)
  print()
  
  print("List:", B)
  func.list_divide(B, 5)
  print("Divide (5):", B)
  print()
  
  B = [-12,-334,64,32,-13,234]
  print("List:", A)
  print("List:", B)
  func.vector_add(B, A)
  print("Vector Add:", B)
  print()
  
  A = [12,334,-64,-32,13,-234]
  B = [-12,-334,64,32,-13,234]
  
  func.eleven()
  print()
  
  print("List:", A)
  print("Big list (10):", func.big_list(A, 10))
  print()