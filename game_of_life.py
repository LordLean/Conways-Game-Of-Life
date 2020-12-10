import numpy as np
import random
import copy
import sys, argparse
import time
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from seeds import seed_collection

class Creature:
  
  WIDTH = 1
  HEIGHT = 1

  def __init__(self, x_pos, y_pos, colour="black"):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.colour = colour
    self.alive = False
    self.neighbours = 0

  # For initial text based GOL.
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
    """
    Fill "board" with creatures.
    """
    for row_index in range(self.x_bounds):
      for column_index in range(self.y_bounds):
        self.board[row_index][column_index] = Creature(row_index, column_index)

  def __seed(self, seed):
    """
    Set seed of initial alive creatures.
    """
    if seed:
      for (x,y) in seed:
        self.board[x][y].alive = True
    else:
      for row_index in range(self.x_bounds):
        for column_index in range(self.y_bounds):
          rand = random.uniform(0,1)
          if rand > 0.8:
            self.board[row_index][column_index].alive = True

  
  def get_neighbours(self, creature):
    """
    Get count of all neighbours for a given (dead or alive) creature.
    """
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
    """
    Return boolean determining whether a creature would survive or come alive in the generation.
    """
    survive = False
    neighbour_count = self.get_neighbours(creature)
    if creature.alive and neighbour_count in [2,3]:
     survive = True
    elif not creature.alive and neighbour_count ==3:
      survive = True
    return survive


  def next_generation(self):
    """
    Create the next generation, creatures' lives subject to Conway's rules.
    """
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
    """
    Text based output. 
    """
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


"""
Matplotlib animation library works best with non-object types. Convert Creatures to 255(on) or 0(off).
Creatures remain as objects incase this project later pursues alternative routes.
"""
def initial(environment):
  copied = np.zeros((environment.x_bounds, environment.y_bounds),dtype=float)
  for row_index in range(environment.x_bounds):
    for col_index in range(environment.y_bounds):
      creature = environment.board[row_index][col_index]
      if creature.alive:
        copied[row_index][col_index] = 255
      else:
        copied[row_index][col_index] = 0
  return copied
def update(frameNum, img, environment):
  environment.next_generation()
  copied = np.zeros((environment.x_bounds, environment.y_bounds),dtype=float)
  for row_index in range(environment.x_bounds):
    for col_index in range(environment.y_bounds):
      creature = environment.board[row_index][col_index]
      if creature.alive:
        copied[row_index][col_index] = 255
      else:
        copied[row_index][col_index] = 0
  img.set_data(copied)
  return img,


def main():
  # Get CLI args.
  parser = argparse.ArgumentParser(description="Conway Game of Life Simulation")
  # add args.
  parser.add_argument("--grid_size", dest="grid_size", required=False)
  parser.add_argument("--seed", dest="seed", required=False)
  parser.add_argument("--interval", dest="interval", required=False)
  parser.add_argument("--save_file", dest="save_file", required=False)
  parser.add_argument("--cmap", dest="cmap", required=False)
  args = parser.parse_args()
  
  # Set grid/board size for environment.
  grid_size = 40
  if args.grid_size:
    grid_size = int(args.grid_size)

  # Set seed - imported froms seeds.py.
  seed = -1
  if args.seed:
    seed = int(args.seed)
  if seed not in seed_collection.keys():
    seed = -1
  seed_name = seed_collection[seed][0]
  seed = seed_collection[seed][1]

  # Create GOL environment.
  env = Environment(grid_size,grid_size,seed)

  interval = 10
  if args.interval:
    interval = int(args.interval)

  cmap = "gray"
  if args.cmap:
    cmap = args.cmap

  # Initial 2d array.
  grid = initial(env)
  # set up animation
  fig, ax = plt.subplots(num=seed_name)
  img = ax.imshow(grid, interpolation='nearest',cmap=cmap)
  ani = animation.FuncAnimation(fig, update, fargs=(img, env, ),
                                frames = 100,
                                interval=interval,
                                save_count=sys.maxsize)
  
  plt.axis("off")

  # If save, the CLI - "args.save_file" str will be the output .gif's name.
  if args.save_file:
    file_name = args.save_file + ".gif"
    ani.save(file_name, fps=10)

  plt.show()


if __name__ == "__main__":
  main()