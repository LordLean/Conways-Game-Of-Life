import numpy as np
import random
import copy
import sys
import time

class Creature:
  
  WIDTH = 1
  HEIGHT = 1

  def __init__(self, x_pos, y_pos, colour="black"):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.colour = colour
    self.alive = False
    self.neighbours = 0

  def draw_creature(self, x, y, colour):
    NotImplemented

  def __repr__(self):
    if self.alive:
      return "X"
    else:
      return "O"

class Environment:

  def __init__(self, x_range, y_range, seed):
    self.x_bounds = x_range
    self.y_bounds = y_range
    self.board = np.zeros((x_range, y_range),dtype=object)
    self.__fill_board()
    self.__seed(seed)
    self.next_board = None
    
  def __fill_board(self):
    for row_index in range(len(self.board)):
      for column_index in range(len(self.board[0])):
        self.board[row_index][column_index] = Creature(row_index, column_index)

  def __seed(self, seed):
    for (x,y) in seed:
      self.board[x][y].alive = True

  
  def get_neighbours(self, creature):
    neighbour_count = 0
    x, y = creature.x_pos, creature.y_pos
    for row_slice in [x-1, x, x+1]:
      for column_slice in [y-1, y, y+1]:
        if row_slice in range(self.x_bounds) and column_slice in range(self.y_bounds):
          if self.board[row_slice][column_slice].alive:
            neighbour_count += 1
    if creature.alive:
      neighbour_count -= 1
    return neighbour_count


  def survived(self, creature):
    survive = False
    neighbour_count = self.get_neighbours(creature)
    if creature.alive and neighbour_count in [2,3]:
     survive = True
    elif not creature.alive and neighbour_count ==3:
      survive = True
    return survive


  def next_generation(self):
    self.next_board = copy.deepcopy(self.board)
    for row in self.board:
      for creature in row:
        x, y = creature.x_pos, creature.y_pos
        if self.survived(creature):
          self.next_board[x][y].alive = True
        else:
          self.next_board[x][y].alive = False
    self.board = self.next_board


  def run_simulation(self, epochs=10,print_=False):
    print("Initial Seed")
    self.print_board()
    for epoch in range(epochs):
      time.sleep(0.1)
      self.next_generation()
      if print_:
        print("Epoch: {}".format(epoch+1))
        self.print_board()


  def print_board(self):
    for row in self.board:
      print(str(row))
    print()


# Glider
seed_glider = [(2,2),(3,3),(4,1),(4,2),(4,3)]

# Penta-decathlon
seed_penta_decathlon = [(8,15),
(9,15),
(10,14),(10,15),(10,16),
(13,14),(13,15),(13,16),
(14,15),
(15,15),
(16,15),
(17,15),
(18,14),(18,15),(18,16),
(21,14),(21,15),(21,16),
(22,15),
(23,15)
]

# Methuselah: R-pentomino
seed_r_pentomino = [(15,15),(15,16),
(16,14),(16,15),
(17,15)]


# Seed choice:
seed = None
seed_choice = int(sys.argv[1])
if seed_choice == 1:
  seed = seed_penta_decathlon
elif seed_choice == 2:
  seed = seed_r_pentomino
else:
  seed = seed_glider
  
# CLI - number of epochs to run for.
epochs = int(sys.argv[2])

board_size = 30
env = Environment(board_size,board_size,seed)


# epochs = 10
print("Epochs Evolved: {}".format(epochs))
env.run_simulation(epochs,True)
