import random

# List of Pokemon cities.
pokemon_cities = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Meowth', 'Psyduck', 'Jigglypuff', 'Geodude', 'Gyarados', 'Eevee', 'Snorlax', 'Pidgey', 'Rattata', 'Weedle', 'Caterpie', 'Spearow', 'Zubat', 'Nidoran', 'Oddish', 'Poliwag', 'Abra', 'Machop', 'Bellsprout', 'Tentacool', 'Ponyta']

# Distance between each city, assuming it is symmetric and the distance between a city to itself is 0
# In actual application this should be replaced with actual data
pokemon_distances = {city:{city:0 for city in pokemon_cities} for city in pokemon_cities}
for city1 in pokemon_cities:
    for city2 in pokemon_cities:
        if city1 != city2:
            pokemon_distances[city1][city2] = random.randint(50, 500) # Randomly assigning distance between cities

# Function to generate a population of possible paths
def generate_population(psize, indiv_size):
    # Initializing the population list
    population = []
    for i in range(psize):
        # Append a randomly sampled path to the population list
        population.append(random.sample(pokemon_cities, indiv_size))
    # Return the population list
    return population

# Function to calculate the fitness of an individual path
def calculate_individual_fitness(individual):
    # Initialize total distance to 0
    total_distance = 0
    for i in range(len(individual) - 1):
        # Add distance between two consecutive cities in the path
        total_distance += pokemon_distances[individual[i]][individual[i + 1]]
    # Add distance from the last city to the first city to complete the circuit
    total_distance += pokemon_distances[individual[-1]][individual[0]]
    # Return negative total distance as fitness. We negate the distance because we want to minimize it, but the genetic algorithm is designed to maximize fitness
    return -total_distance  

# Function to calculate the probability of selection for each individual in the population
def set_probabilities_of_population(population):
    # Calculate the fitness of each individual
    fitnesses = [calculate_individual_fitness(individual) for individual in population]
    # Calculate total fitness of the population
    total_fitness = sum(fitnesses)
    # Calculate probability of selection for each individual
    probabilities_of_selection = [fitness / total_fitness for fitness in fitnesses]
    # Return list of probabilities
    return probabilities_of_selection

# Function to select a number of individuals from the population using roulette wheel selection
def roulette_wheel_selection(population, number_of_selections):
    # Calculate the probability of selection for each individual
    probabilities = set_probabilities_of_population(population)
    # Initialize the list of selected individuals
    selected = []
    # Perform roulette wheel selection
    for _ in range(number_of_selections):
        # Generate a random number for the roulette wheel
        spin = random.uniform(0, 1)
        total = 0
        # Loop over the population
        for i, probability in enumerate(probabilities):
            # Increase the cumulative probability
            total += probability
            # If the cumulative probability exceeds the roulette wheel number, select this individual
            if spin <= total:
                # Add the selected individual to the list
                selected.append(population[i])
                break
    # Return the list of selected individuals
    return selected

# Function to perform a one-point crossover operation on two parent paths
def one_point_crossOver(parentA, parentB):
    # Get the length of the parent path
    length = len(parentA)
    # If the length is less than 3, return the parents as they are
    if length < 3:
        return parentA, parentB
    # Randomly select a crossover point (cut) between 1 and length - 1
    cut = random.randint(1, length - 1)
    # Take the segment before the cut from each parent
    keepA = parentA[:cut]
    keepB = parentB[:cut]
    # Create the first child by appending cities from parentB to keepA ensuring no city is repeated
    childA = keepA + [city for city in parentB if city not in keepA]
    # Create the second child by appending cities from parentA to keepB ensuring no city is repeated
    childB = keepB + [city for city in parentA if city not in keepB]
    # Return the two children
    return childA, childB

# Function to mutate an individual path
def mutate_individual(individual):
    # Swap mutation: randomly select two cities and swap their places
    # This adds variability to the population
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Function to calculate the fitness of the whole population
def calculate_population_fitness(population):
    # Calculate and return the minimum of the negative fitness values of the individuals
    # Negative fitness is used because we're minimizing the total path length
    return min(-calculate_individual_fitness(individual) for individual in population)

# Function to generate children from the selected parents
def reproduce_children(chosen):
    # Initialize the children list
    children = []
    # Loop over the chosen parents in pairs
    for i in range(0, len(chosen), 2):
        # Generate two children by performing one-point crossover on a pair of parents
        childA, childB = one_point_crossOver(chosen[i], chosen[i+1])
        # Add the children to the children list
        children.extend([childA, childB])
    return children

# Function to apply mutation to the children
# Function to apply mutation to each child in a list of children
def mutate_children(children):
    # Apply the mutate_individual function to each child in the list
    # This allows to introduce variability into the new generation
    return [mutate_individual(child) for child in children]

# Function to run the genetic algorithm for a certain number of generations
def run_ga(psize, number_of_generations):
    # Generate an initial population
    global_population = generate_population(psize, len(pokemon_cities))

    # Initialize the best global distance to infinity
    best_global_distance = float('inf')
    # Initialize the best global path to None
    best_global_path = None

    # Run the algorithm for the given number of generations
    for generation in range(number_of_generations):
        # Calculate the best distance in the current population
        current_best_distance = calculate_population_fitness(global_population)
        # If this distance is better than the best global distance, update the best global distance
        # print(f"Generation {generation+1}: Current best distance: {current_best_distance}") #remove this
        if current_best_distance < best_global_distance:
            best_global_distance = current_best_distance
            # print(f"New best global distance: {best_global_distance}") #remove this

        # Perform roulette wheel selection to choose individuals for reproduction
        the_chosen = roulette_wheel_selection(global_population, psize)
        # Generate children from the chosen individuals
        the_children = reproduce_children(the_chosen)
        # Mutate the children
        the_children = mutate_children(the_children)
        # Replace the old population with the new children
        global_population = the_children  

        # Track the path, not just the distance:
        # Identify the path with the best fitness in the current population
        current_best_path = min(global_population, key=calculate_individual_fitness)
        # If this path is better than the best global path, update the best global path
        if best_global_path is None or calculate_individual_fitness(current_best_path) < calculate_individual_fitness(best_global_path):
            best_global_path = current_best_path
            # print(f"New best global path: {best_global_path}") #remove this

    # Return the best global distance and the best global path
    return best_global_distance, best_global_path


def main():
    random.seed(25)
    psize = 50
    number_of_generations = 500

    best_global_distance, best_global_path = run_ga(psize, number_of_generations)
    print(f"The best global distance achieved after {number_of_generations} generations is: {best_global_distance}")
    print(f"The best path is: {best_global_path}")

if __name__ == "__main__":
    main()
