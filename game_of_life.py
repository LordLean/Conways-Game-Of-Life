# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
import numpy as np
import random
import copy

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
    for epoch in range(epochs):
      self.next_generation()
      if print_:
        print("Epoch: {}".format(epoch))
        self.print_board()


  def print_board(self):
    for row in self.board:
      print(str(row))
    print()

# seed = [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
seed = [(2,2),(3,3),(4,1),(4,2),(4,3)]

board_size = 20
env = Environment(board_size,board_size,seed)

print("Starting Board")
env.print_board()

epochs = 10
print("Epochs Evolved: {}".format(epochs))
env.run_simulation(epochs,True)

# board_size = 20
# env = Environment(board_size,board_size)

# creature = env.board[2][2]
# creature.alive = True

# creature1 = env.board[1][1]
# # creature1.alive = True
# creature2 = env.board[1][2]
# # creature2.alive = True
# creature3 = env.board[1][3]
# # creature3.alive = True

# creature4 = env.board[2][1]
# creature4.alive = True
# # creature5 = env.board[1][2]
# # creature5.alive = True
# creature6 = env.board[2][3]
# creature6.alive = True

# creature7 = env.board[3][1]
# # creature7.alive = True
# creature8 = env.board[3][2]
# # creature8.alive = True
# creature9 = env.board[3][3]
# # creature9.alive = True

# print("Starting Board")
# env.print_board()

# epochs = 3
# print("Epochs Evolved: {}".format(epochs))
# env.run_simulation(epochs)
# env.print_board()

#######################################################

# def draw_creature(x,y, colour="black"):
#   return patches.Rectangle((x,y),1,1,color=colour)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# # Major ticks every 20, minor ticks every 5
# major_ticks = np.arange(0, 101, 20)
# minor_ticks = np.arange(0, 101, 5)

# ax.set_xticks(major_ticks)
# ax.set_xticks(minor_ticks, minor=True)
# ax.set_yticks(major_ticks)
# ax.set_yticks(minor_ticks, minor=True)

# # And a corresponding grid
# ax.grid(which='both')

# # Or if you want different settings for the grids:
# ax.grid(which='minor', alpha=0.8)
# ax.grid(which='major', alpha=1)

# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(15, 15)

# rect2 = draw_creature(10,10,"red")
# ax.add_patch(rect2)

# for x in range(0,100,1):
#   rect = draw_creature(x,x)
#   ax.add_patch(rect)

# plt.show()
