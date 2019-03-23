from GA.genetic_algorithms import GeneticAlgorithm
import random

class DataProcess:
    """
    :param decimal_number: 传入十进制数
    """
    def __init__(self,decimal_number:int):
        self.decimal_number = decimal_number

    @classmethod
    def from_binary_str(cls, binary: str):
        return DataProcess(int(binary, 2))


    def __str__(self) -> str:
        # print(1)
        """
        如果要把一个类的实例变成 str，就需要实现特殊方法__str__()
        :return: 将传入的十进制数转换成二进制:str
        """
        return '{:06b}'.format(self.decimal_number)


    def __repr__(self):
        # print(2)
        # repr返回一个对象的string格式
        return repr(self.decimal_number)

class QuadraticSolotion(GeneticAlgorithm):

    def __init__(self,equation, boundary:(int,int), generations=5, population_size=4, find_min: bool=True):
        GeneticAlgorithm.__init__(self, generations=generations)
        self._quadratic_eq = equation
        self._lower_bound, self._upper_bound = boundary
        self._population_size = population_size
        self.reverse_sort = find_min
        assert self._lower_bound < self._upper_bound

    def _initiate_first_population(self) -> [DataProcess]:
        return [DataProcess(random.randint(self._lower_bound,self._upper_bound)) for _ in range(self._population_size)]

    def _crossover(self,chromosome1:DataProcess,chromosome2:DataProcess) -> DataProcess:
        offspring = ''
        for gene1,gene2 in zip(str(chromosome1),str(chromosome2)):
            if random.randint(0,100) < self.crossover_rate:
                offspring += gene1
            else:
                offspring += gene2
        return DataProcess(int(offspring,2))

    def _mutation(self,chromosome:DataProcess) -> DataProcess:
        mutation_formula = lambda x:'0' if x=='1' else '1'
        result = ''
        # result =''.join(mutation_formula(bit) if random.randint(0,100) < self.mutation_rate else bit for bit in str(chromosome))
        for bit in str(chromosome):
            if random.randint(0,100) < self.mutation_rate:
                bit = mutation_formula(bit)
            result += bit

        return DataProcess(int(result,2))

    def _evaluate(self,chromosome:DataProcess):
        return self._quadratic_eq(chromosome.decimal_number)

    def _is_vaild(self,chromosome:DataProcess)->bool:
        return self._upper_bound >= chromosome.decimal_number >= self._lower_bound

