import sys
import random
from TravellingSalesman import TravellingSalesman


class GeneticAlgorithm(TravellingSalesman):

    def __init__(self, input_file):
        super().__init__(input_file)
        self.population_size = 50
        # percent mutation probability for each child
        self.mutation_prob = 0.1

    def init_population(self):
        """
        Initializes the population
        """
        population = set()
        while len(population) != self.population_size:
            population.add(tuple(self.random_tour()))
        return [list(tour) for tour in population]

    def calculate_fitness(self, population):
        """
        Return a fitness list for the population
        Fitness is just 1 / eval(tour)
        """
        fitness = [1 / self.eval(tour) for tour in population]
        sum_fitness = sum(fitness)
        return [f / sum_fitness for f in fitness]

    def order_crossover(self, parent1, parent2):
        """
        Implements order crossover operator
        """
        start = random.randint(0, self.num_of_cities - 2)
        end = random.randint(start, self.num_of_cities - 1)
        child1 = parent1[start:end]
        child2 = parent2[start:end]
        for city in parent1:
            if city not in child2:
                child2.append(city)
        for city in parent2:
            if city not in child1:
                child1.append(city)
        return [child1, child2]

    def cycle_crossover(self, parent1, parent2):
        """
        Implements cycle crossover operator
        """
        child1 = [-1] * self.num_of_cities
        child2 = child1.copy()

        i = 0
        while child1[i] == -1:
            child1[i] = parent1[i]
            i = parent1.index(parent2[i])

        i = 0
        while child2[i] == -1:
            child2[i] = parent2[i]
            i = parent2.index(parent1[i])

        for i in range(self.num_of_cities):
            if child1[i] == -1:
                child1[i] = parent2[i]

            if child2[i] == -1:
                child2[i] = parent1[i]
        return [child1, child2]        

    def mutate(self, child):
        """
        Given a child will exchange any two cities
        """
        return self.random_neighbour(child)

    def genetic_algorithm(self):
        population = self.init_population()
        for _ in range(1000):
            # selection
            fitness = self.calculate_fitness(population)
            selected = random.choices(population, fitness, k=self.population_size)
            random.shuffle(selected)

            # offsprings
            offsprings = []
            for i in range(self.population_size // 2):
                children = self.order_crossover(population[i], population[i + self.population_size // 2])
                offsprings.extend(children)

            # mutation
            for index in range(self.population_size):
                if random.uniform(0, 1) < self.mutation_prob:
                    offsprings[index] = self.mutate(offsprings[index])

            # replacement
            population.extend(offsprings)
            fitness = self.calculate_fitness(population)
            population = [tour for _, tour in sorted(zip(fitness, population), reverse=True)]
            population = population[:self.population_size]
        return population[0]


def main():
    tsp = GeneticAlgorithm(sys.argv[1])
    tour = tsp.genetic_algorithm()
    tsp.print_tour(tour)


if __name__ == "__main__":
    main()
