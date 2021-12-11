def print_recur(root):
  if root:
    print(root.data)
    print_recur(root.next)

class Chain:
  head = None
  def __init__(self, data = 0):
    self.data = data
    self.next = None

  def generateChain(self, L):
    if len(L) == 0:
      return
    else:
      data = L[0]
      L.pop(0)
      if self.head == None:
        self.head = Chain(data)
      else:
        temp = self.head
        while temp.next != None:
          temp = temp.next
        temp.next = Chain(data)
      self.generateChain(L)
      
  def print_chain(self):
    print_recur(self.head)



def main():
  C = Chain()
  C.generateChain([1,2,3])
  C.print_chain()

main()



