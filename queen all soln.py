def initialize(n):
  board['queen']=[]
  for key in ['row','col','nwtose','swtone']:
        board[key] = {}
  for i in range(n):
    board['row'][i] = 0
    board['col'][i] = 0
  for i in range(-(n-1),n):
    board['nwtose'][i] = 0
  for i in range(2*n-1):
    board['swtone'][i] = 0

def printboard():
  for row in range(len(board['queen'])):
    print (row+1,board['queen'][row]),
  print("")

def free(i,j):
  return(board['row'][i] == 0 and board['col'][j] == 0 and
          board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i,j):
  board['queen'].append(j)
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j):
  board['queen'].pop()
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

solution = 0

def placequeen(i):
  global solution
  for j in range(n):
    if free(i,j):
      addqueen(i,j)
      if i == n-1:
        printboard()
        solution = solution+1
      else:
        placequeen(i+1)
      undoqueen(i,j)


board = {}
n = int(input("How many queens? "))
initialize(n)
placequeen(0)
print "total no. of solutions are: ",solution