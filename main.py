import check_input

# Function that reads the file of the maze and inserts it into a list
def read_maze(maze):
  file = open(maze)

  list_2D = []
  # iterates through every row of the txt file
  for row in file:
    list =[]
    # Appends every item in the row to a new list.
    for item in row:
      if item != '\n':
        list.append(item)
    list_2D.append(list)
  return list_2D      

#function to find the start in the maze which is the 2d list, and the start is denoted by an s
def find_start(maze):
  #nested loop to iterate through each character in each line
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      #checks if the current character is an s and if so saves the location and terminates the loop
      if maze[i][j] == 's':
        return [i, j]

# Reads the list created in (read_maze) and gets the coordiates received in (find_start) to generate the maze
def display_maze(maze, loc):
  for i in range(len(maze)):
    print()
    for j in range(len(maze[i])):
      if i == loc[0] and j == loc[1]:
        print('X', end='')
      else:
        print(maze[i][j], end='')

def main():
  #initializes the maze the user location and the value to determine whether to stop the loop
  maze = read_maze('maze2-1.txt')
  user_loc = find_start(maze)
  done = True
  print('-Maze Solver-')
  #loop that continues until the user reaches the end of the maze
  while done:
    okay = True
    display_maze(maze, user_loc)
    #loop that continues until the user enters a proper answer to move and updates user position in the maze
    while okay:
      choice = check_input.get_int_range('\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n', 1, 4)
      if choice == 1:
        if maze[user_loc[0] - 1][user_loc[1]] == '*':
          print('You cannot move there')
        else:
          user_loc[0] -= 1
          okay = False

      elif choice == 2:
        if maze[user_loc[0] + 1][user_loc[1]] == '*':
          print('You cannot move there')
        else:
          user_loc[0] += 1
          okay = False

      elif choice == 3:
        if maze[user_loc[0]][user_loc[1] + 1] == '*':
          print('You cannot move there')
        else:
          user_loc[1] += 1
          okay = False

      elif choice == 4:
        if maze[user_loc[0]][user_loc[1] - 1] == '*':
          print('You cannot move there')
        else:
          user_loc[1] -= 1
          okay = False
    #checks if the user has reached the end of the maze and terminates the loop if so
    if maze[user_loc[0]][user_loc[1]] == 'f':
      print('Congratulations! You solved the maze.')
      done = False
main()