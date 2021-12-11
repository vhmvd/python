from os import name
from tkinter.constants import CURRENT
import xlrd
from Linklist import Node
from queue import Queue

class file_read:
  file_name        = "LondonUndergroundData.xlsx"
  line_and_station = list()
  scanned          = list()
  stations         = list()
  head             = 0
  current          = 0
  def file_read(self):
    """Reads the xlsx file
    """
    work_book  = xlrd.open_workbook(self.file_name)
    work_sheet = work_book.sheet_by_index(0)
    for itr in range(work_sheet.nrows):
      temp_list = work_sheet.row_values(itr)
      if(temp_list[2] == "") and (temp_list[3] == ""):
        if temp_list[1] not in self.stations:
          self.stations.append(temp_list[1].strip())
      else:
        self.line_and_station.append([temp_list[0].strip(), temp_list[1].strip(), temp_list[2].strip(), temp_list[3]])

  def create_nodes(self):
    """Creates doubly linked list from line_and_station
    """
    self.head = 0
    for itr in range(0, len(self.line_and_station)):
      if (self.line_and_station[itr][0]+self.line_and_station[itr][1]) in self.scanned:
        continue
      if itr == 0:
        node      = Node(self.line_and_station[0][1], self.line_and_station[0][0])
        self.head = node
        self.current   = self.head
      elif itr == 1:
        node = Node(self.line_and_station[itr][1], self.line_and_station[itr][0])
        node.set_prev_node(self.head)
        self.head.set_next_node(node)
        self.current = node
      else:
        node = Node(self.line_and_station[itr][1],  self.line_and_station[itr][0])
        self.current.set_next_node(node)
        node.set_prev_node(self.current)
        self.current = node

      if self.line_and_station[itr][1] not in self.scanned:
        self.scanned.append(self.line_and_station[itr][0]+self.line_and_station[itr][1])

        node.set_edges([self.line_and_station[itr][2], self.line_and_station[itr][3]])

        for itr2 in range(itr+1, len(self.line_and_station)):
          if self.line_and_station[itr][1] == self.line_and_station[itr2][1]:
            flag = True
            for itr3 in node.edges:
              if itr3[0] == self.line_and_station[itr2][2]:
                flag = False
                break
            if flag:
              node.set_edges([self.line_and_station[itr2][2], self.line_and_station[itr2][3]])

  def create_nodes_again(self):
    self.head = 0
    for itr in range(0, len(self.line_and_station)):
      if (self.line_and_station[itr][0]+self.line_and_station[itr][1]) in self.scanned:
        continue
      if itr == 0:
        node      = Node(self.line_and_station[0][1], self.line_and_station[0][0])
        self.head = node
        self.current   = self.head
      elif itr == 1:
        node = Node(self.line_and_station[itr][1], self.line_and_station[itr][0])
        node.set_prev_node(self.head)
        self.head.set_next_node(node)
        self.current = node
      else:
        node = Node(self.line_and_station[itr][1],  self.line_and_station[itr][0])
        self.current.set_next_node(node)
        node.set_prev_node(self.current)
        self.current = node

      if self.line_and_station[itr][1] not in self.scanned:
        self.scanned.append(self.line_and_station[itr][0]+self.line_and_station[itr][1])

        node.set_edges([self.line_and_station[itr][2], self.line_and_station[itr][3]])

        for itr2 in range(itr+1, len(self.line_and_station)):
          if self.line_and_station[itr][1] == self.line_and_station[itr2][1]:
            flag = True
            for itr3 in node.edges:
              if itr3[0] == self.line_and_station[itr2][2]:
                flag = False
                break
            if flag:
              node.set_edges([self.line_and_station[itr2][2], self.line_and_station[itr2][3]])

  def algorithm(self, start, end, time):
    """Takes the starting and ending from gui and computes the path

    Args:
        start (String): [Starting Node]
        end (String): [Ending Node]


    Returns:
        [List]: [List of explored route from starting to end]
    """
    if start and end not in self.stations:
      return []
    queue = Queue()
    routeQueue = Queue()
    timeQueue = Queue()
    timeQueue.put(0)
    queue.put(start)
    explored = []
    nodePtr = self.head
    flag = False
    current_station = start
    while queue.empty() == False and current_station!=end:
      if current_station == end:
        continue

      current_station = queue.get()
      temp = self.head
      if current_station not in explored:
        explored.append(current_station)
      while current_station != temp.get_name():
        temp = temp.next_node
        if temp == None:
          return

      if flag:
        if nodePtr:
          for itr in nodePtr.route:
            temp.route.append(itr)
        st = routeQueue.get()
        if st not in nodePtr.route:
          temp.route.append(st)
        nodePtr = temp
      else:
        nodePtr = temp
        flag = True
            
      for itr in temp.edges:
        if itr[0] not in explored:
          queue.put(itr[0])
          timeQueue.put(itr[1])
          routeQueue.put([temp.line, temp.name, timeQueue.get()])

    temp = self.head
    while end != temp.get_name():
      temp = temp.next_node
    temp.route.append([temp.line, temp.name, timeQueue.get()])
    return temp.route

    
