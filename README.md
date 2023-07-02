# Traveling_Salesman-Problem
exploring genetic algorithms and utilizing the algorithm on TSP.
# Pokemon City Travelling Salesman Problem

This Python script attempts to solve a version of the Travelling Salesman Problem (TSP) using a Genetic Algorithm. The cities in this context are fictional Pokemon cities.

## Problem Description

The TSP is an optimization problem that seeks to find the shortest possible route a travelling salesman can take to visit every city once and return to the original city. In this script, each city is represented by the name of a Pokemon, and the "distance" between two cities is a random integer between 50 and 500.

## How to Run

1. Ensure you have Python 3.x installed on your machine. You can download it from [here](https://www.python.org/downloads/).

2. Clone this repository to your local machine or download the script.

3. Run the script from the command line or your preferred Python integrated development environment (IDE). In the command line, navigate to the directory containing the script and run:

   ```shell
   python pokemon_tsp.py
   ```

## Script Explanation

The script contains the following functions:

- `generate_population(psize, indiv_size)`: Generates a population of possible paths.

- `calculate_individual_fitness(individual)`: Calculates the fitness of an individual path.

- `set_probabilities_of_population(population)`: Calculates the probability of selection for each individual in the population.

- `roulette_wheel_selection(population, number_of_selections)`: Selects a number of individuals from the population using roulette wheel selection.

- `one_point_crossOver(parentA, parentB)`: Performs a one-point crossover operation on two parent paths.

- `mutate_individual(individual)`: Mutates an individual path.

- `calculate_population_fitness(population)`: Calculates the fitness of the entire population.

- `reproduce_children(chosen)`: Generates children from the selected parents.

- `mutate_children(children)`: Applies mutation to each child in a list of children.

- `run_ga(psize, number_of_generations)`: Runs the genetic algorithm for a certain number of generations.

- `main()`: The main function that coordinates the operations of the script. 

The script can be customized by adjusting parameters such as the population size (`psize`) and the number of generations (`number_of_generations`). 

## Output

The script outputs the best global distance (i.e., the shortest total distance achieved) and the path taken to achieve this distance. This is output after the specified number of generations are run in the genetic algorithm.

## Note

This is a simplified version of the TSP and the distances between cities are randomly generated. For a more accurate representation of a real-world TSP, more realistic distances could be used.

The genetic algorithm implemented here is a simple version and does not include some features that could potentially improve performance, such as elitism (i.e., directly carrying the best individuals from one generation to the next) or more advanced crossover and mutation techniques.
