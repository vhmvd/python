
def loadQuestions():
    
  qs = []

  s = '\n'
  q = ''
  ans = ''
  options = []
  
  with open('animals.txt') as file:
    for s in file:
      ls = s.split()
      if len(ls) == 0:
        if q != '':
          if len(options) == 2:
            if ans == 'Yes' or ans == 'True':
              qs.append([q, True])
            if ans == 'No' or ans == 'False':
              qs.append([q, False])
          q = ''
          ans = ''
          options = []
      else:
        t = ' '.join(ls[1:])
        if ls[0] == '#Q':
          q = t
        elif ls[0] == '^':
          ans = t
        else:
          options.append(t)
  return qs

