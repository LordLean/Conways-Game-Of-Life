# Conways-Game-Of-Life

## WARNING - Game of Life simulation below is shown by black and white .gifs. Contrasting dark and light spaces may be unsuitable for some.

Python implementation of Conway's game of life. 0-player game where evolution is determined by the population's seed. Animation is handled using Matplotlib.animation.FuncAnimation().

Seeds are held in "seeds.py" in dictionary form: seed_collection -> {\<key value\>: [\<seed name\>, <seed's list of tuples>]}. Add new seeds above the collection and save reference in the seed_collection dictionary with new key and seed name (this is used for the output's title). 

Example: 

![](https://raw.githubusercontent.com/LordLean/Conways-Game-Of-Life/main/Images/random_one.gif)
![](https://raw.githubusercontent.com/LordLean/Conways-Game-Of-Life/main/Images/fun_one.gif)

There are five command line arguments:
* "--grid_size" INT -> This corresponds to the x by y square board that the game of life takes place on.
* "--seed" INT -> A numerical value to determine which seed to initialize GOL with. Default is -1 which corresponds to random spawn. Approx 0.2 of all creatures will start alive.
* "--interval" INT -> Delay between output frames in milliseconds.
* "--save_file" STR -> The desired file name for saving animation to .gif.
* "--cmap" STR -> Set the matplotlib colour map for prettier visuals.
  * https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
  * Hopefully in future there will be more rules which create objects of varying colour rather than 0 and 255.
  
Gray Cmap            |  Ocean Camp
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/LordLean/Conways-Game-Of-Life/main/Images/fun2.png)  |  ![](https://raw.githubusercontent.com/LordLean/Conways-Game-Of-Life/main/Images/fun_ocean.png)
