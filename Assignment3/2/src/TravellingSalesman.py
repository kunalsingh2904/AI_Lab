import sys
import random


class TravellingSalesman():

    def __init__(self, input_file):
        """
        Read the input file
        distance_matrix: stores the distance between two cities
        distance_matrix[i][j] gives distance between city i and city j
        """
        with open(input_file) as fp:
            lines = fp.readlines()
            self.num_of_cities = int(lines[1])

            self.cities = []
            for line in lines[2:self.num_of_cities + 2]:
                city = line.strip().split(' ')
                self.cities.append(tuple(city))

            self.distance_matrix = []
            for dist in lines[self.num_of_cities + 2:]:
                distance = dist.strip().split(' ')
                self.distance_matrix.append([float(x) for x in distance])

    def random_tour(self):
        """
        Returns a random valid tour
        """
        tour = list(range(self.num_of_cities))
        random.shuffle(tour)
        return tour

    def eval(self, tour):
        """
        Calculates cost of a tour
        """
        cost = 0
        for i in range(self.num_of_cities):
            cost += self.distance_matrix[tour[i]][tour[(i+1) % self.num_of_cities]]
        return cost

    def random_neighbour(self, tour):
        """
        Two city exchange
        """
        new_tour = tour.copy()
        random_city = random.sample(range(self.num_of_cities), 2)
        new_tour[random_city[0]], new_tour[random_city[1]] = tour[random_city[1]], tour[random_city[0]]
        return new_tour

    def print_tour(self, tour):
        """
        Prints the tour and the cities
        """
        print(self.eval(tour))
        print(' '.join(str(city) for city in tour))
        # for city in tour:
        #     print(self.cities[city][0] + " " + self.cities[city][1])


def main():
    tsp = TravellingSalesman(sys.argv[1])


if __name__ == "__main__":
    main()
