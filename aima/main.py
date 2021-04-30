import numpy as np
import csv
from math import log

class tree:
  def __init__(self, sample_filename, label_list):
    self.data = self.parse_data(sample_filename, label_list)
    self.split_variable      = label_list[-1]
    self.data_attribute      = label_list[:-1]
    self.attribute_variables = self.create_values_dictionary()
    self.head_node           = Node()
    self.depth               = None
    
  def parse_data(self, file_name, labels):
    """Parse the csv file

    Args:
        file_name (string)
        labels (strings)

    """
    data = open(file_name)
    data_reader = csv.reader(data)
    matrix = []
    for row in data_reader:
      new_dict = {}
      for i in range(len(row)):
        row[i] = row[i].strip()
        if row[i] == 'Yes':
          row[i] = True
        elif row[i] == 'No':
          row[i] = False
        new_dict[labels[i]] = row[i]
      matrix.append(new_dict)
    return matrix
  
  def create_values_dictionary(self):
    """Creates the datastructure
    """
    temp_dict = {}
    for i in range(len(self.data_attribute)):
      k = self.data_attribute[i]
      temp_dict[k] = []
      for j in range(len(self.data)):
        temp_dict[k].append(self.data[j][k])
      temp_dict[k] = list(set(temp_dict[k]))
    return temp_dict
      
  
  def node_entropy(self, samples):
    T, F = 0, 0
    n = len(samples)
    if n == 0:
      return 0
    for i in range(n):
      if (samples[i][self.split_variable] == True):
        T += 1
      else:
        F += 1
    P_T, P_F = T/n, F/n
    if P_T == 0:
      P_T = 1
    if P_F == 0:
      P_F = 1
    
    return -sum([P_T*log(P_T,2), P_F*log(P_F,2)]) # entropy
  
  def split_entropy(self, samples, split_attribute):
    """Function to calculate

    Args:
        samples
        split_attribute
    """
    attribute_values = self.attribute_variables[split_attribute] 
    n = len(samples)
    a = len(attribute_values)
    sample_splits = self.split_data(samples, split_attribute)
    entropy_terms = []
    for i in range(a):
      node_sample_num = len(sample_splits[attribute_values[i]])
      e = self.node_entropy(sample_splits[attribute_values[i]])      
      entropy_terms.append((node_sample_num/n) * e)
    return sum(entropy_terms)
  
  def minimum_split_variable(self, attrs, samples):
    """Find the min variable for split

    Args:
        attrs 
        samples 

    """
    vals = np.zeros(len(attrs))
    for i in range(len(attrs)):
      vals[i] = self.split_entropy(samples, attrs[i])
    idx = np.argmin(vals)
    return attrs[idx]

  def build(self, data, prev_node, attr_list, prev_branch_val= None):
    """Recursive build function

    Args:
        data 
        prev_node
        attr_list
        prev_branch_val ([type], optional): [description]. Defaults to None.
    """
    if self.depth == None: 
      print("please set depth first")
      return    
    if ((len(attr_list) == 0) or (self.depth <= self.node_depth(prev_node))):
      if(len(data) == 0):
        new_node = Node(parent = prev_node, branch_val = prev_branch_val)
        prev_node.children.append(new_node)
        return
      elif(data[0][self.split_variable] == True):
        new_node = Node(parent = prev_node, branch_val = prev_branch_val, leaf = True)
        prev_node.children.append(new_node)
        return
      elif(data[0][self.split_variable] == False):
        new_node = Node(parent = prev_node, branch_val = prev_branch_val, leaf = False)
        prev_node.children.append(new_node)
        return
    
    elif(len(data) == 0): 
      new_node = Node(parent = prev_node, branch_val = prev_branch_val)
      prev_node.children.append(new_node)
      return
    attr = self.minimum_split_variable(attr_list, data)
    attr_list.remove(attr)
    new_node = Node(parent = prev_node, branch_val = prev_branch_val, variable = attr)
    prev_node.children.append(new_node)
    data_splits = self.split_data(data, attr)
    branches = self.attribute_variables[attr]
    for i in range(len(branches)):
      self.build(data_splits[branches[i]], new_node, attr_list, branches[i])
    
  def split_data(self, data, attr):
    attr_vals = self.attribute_variables[attr]
    n = len(data)
    a = len(attr_vals)
    data_splits = {}
    for i in range(a):
      data_splits[attr_vals[i]] = []
    for i in range(n):
      data_splits[data[i][attr]].append(data[i]) 
        
    return data_splits
    
  def node_depth(self, node):
    """Returns depth

    Args:
        node

    Returns:
        [depth]
    """
    d = 0
    while(node.parent != None):
      d += 1
      node = node.parent
      
    return d
  
  def visualize(self, node=None, dictionary = {}):
    '''Returns a dictionary of node descriptions where each key is the depth in
        the tree.'''
    if node == None:
      node = self.head_node
      p_var = None
    else: 
      p_var = node.parent.var
      
    d = self.node_depth(node)
    
    if d in dictionary.keys():
      dictionary[d].append((node.var, 'From Node: ', p_var, 'Through Branch: ', node.branch_val, 'Leaf Value: ', node.leaf)) 
    else:
      dictionary[d] = [(node.var, 'From Node: ', p_var, 'Through Branch: ', node.branch_val, 'Leaf Value: ', node.leaf)]
    
    for i in range(len(node.children)):
      self.visualize(node.children[i], dictionary)
      
    return dictionary
  
  def evaluate(self, sample):
    '''Uses the generated tree structure to classify a sample datapoint.'''
    current = self.head_node.children[0]
    decision = None
    not_leaf = True
    while not_leaf:
      # check if current node is a leaf:
      if not current.children: # will be true when list is empty (leaf node)
        decision = current.leaf
        not_leaf = False
        
      # otherwise figure out which branch to go down:
      else:
        for i in range(len(current.children)):
          if current.children[i].branch_val == sample[current.var]:
            current = current.children[i]
            break
    return decision
    
class Node:
  '''A class representing the nodes of a decision tree.'''
  def __init__(self, parent = None, branch_val = None, variable = None, leaf = None):
    self.parent     = parent
    self.branch_val = branch_val
    self.var        = variable
    self.children   = []
    self.leaf       = leaf

Tree = tree('restaurant.csv', ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res', 'type', 'est', 'wait'])
"""
Alt(ernate), Fri(day), Hun(gry), Pat(rons), Res(ervation), Est(imated waiting time)
"""
Tree.depth = 3
Tree.build(Tree.data, Tree.head_node, Tree.data_attribute)

dictionary = Tree.visualize()
for i in range(1, len(list(dictionary.keys()))): 
  print(dictionary[i], "\n")

count = 0
for i in range(len(Tree.data)):
  actual = Tree.data[i]['wait']
  pred   = Tree.evaluate(Tree.data[i])
  if actual == pred:
    count += 1
print("Accuracy of Training Data: ", count/len(Tree.data))