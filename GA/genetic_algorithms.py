import random
from abc import abstractmethod

class GeneticAlgorithm:

    def __init__(self,generations:int = 100):
        """

        :param generations:
        """
        self.keep_best = True
        self.generations = generations
        self._current_population = []
        self.crossover_rate = 50  # 50%
        self.mutation_rate = 10  # 10%
        self._best_of_generation = None
        self.reverse_sort = False #aescending order = Fasle(default), descending order = True


    @abstractmethod
    def _initiate_first_population(self):
        raise NotImplementedError

    @abstractmethod
    def _crossover(self,chromosome1,chromosome2):
        raise NotImplementedError

    @abstractmethod
    def _mutation(self,chromosome):
        raise NotImplementedError

    @abstractmethod
    def _evaluate(self,chromosome):
        raise NotImplementedError

    @abstractmethod
    def _is_vaild(self, chromosome):
        raise NotImplementedError

    def __choice(self):
        choice_pool = []
        for position,chromosome in enumerate(self._current_population):
            choice_pool.extend([chromosome] * position)
        return choice_pool


    def search(self):
        self._current_population = self._initiate_first_population()

        for i in range(self.generations):
            print("Generation No.{}".format(i))

            # 1. Evaluation phase
            # 根据_evaluate的计算结果排序，使用降序，将代入方程获得最小值排在最后
            self._current_population.sort(key = self._evaluate, reverse=self.reverse_sort)
            print("current_population: {}".format(self._current_population))
            self._best_of_generation = self._current_population[-1]
            print("Best result is {}".format(self._evaluate(self._best_of_generation)))

            next_population = []
            # 是否将上代的最佳基因保留进入下一代
            if self.keep_best:
                next_population.append(self._best_of_generation)

            # 2. Choice phase
            choice_pool_for_mating  = self.__choice()
            # print("choice_pool_for_mating:{}".format(choice_pool_for_mating))

            while len(next_population) < len(self._current_population):

                parent1 = random.choice(choice_pool_for_mating)
                parent2 = random.choice(choice_pool_for_mating)
                # print("parent1:{},{} ; parent2:{},{}".format(parent1,int(str(parent1),2),parent2,int(str(parent2),2)))

                # 3. Crossover
                child = self._crossover(parent1,parent2)
                # print("crossover_child:{},{}".format(child,int(str(child),2)))

                # 4.Mutation
                child = self._mutation(child)
                # print("mutation_child:{},{}".format(child,int(str(child),2)))

                if not self._is_vaild(child):
                    continue

                next_population.append(child)
                # print("next_population:{}".format(next_population))

            self._current_population = next_population


    def get_result(self):
        return self._best_of_generation

# class Gun():
#     def __init__(self,model):
#         self.model = model
#
#     def fire(self):
#         print(123)
#
#     def shoot(self):
#         self.fire()