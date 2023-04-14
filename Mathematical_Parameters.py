from math import sqrt

class Mat_Par:

    __aver_val = 0

    __dis = 0

    __st_dev = 0

    __dev = {}


    def average_value(self, numerical_values):

        for value in numerical_values:

            self.__aver_val += numerical_values[value]

        self.__aver_val //= len(numerical_values)


    def deviation(self, true_values):

        for value in true_values:

            self.__dev.update( { value : true_values[value] - self.__aver_val } )


    def dispersion(self):

        for value in self.__dev:

            self.__dis += self.__dev[value] ** 2

        self.__dis //= len(self.__dev)


    def standard_deviation(self):

        self.__st_dev = round(sqrt(self.__dis))


    def print_average_value(self):

        print("")
        print("Average value: ", self.__aver_val)
        print("")


    def print_deviation(self):

        print("")
        print("Deviation: ", self.__dev)
        print("")


    def print_dispersion(self):

        print("")
        print("Dispersion: ", self.__dis)
        print("")


    def print_standard_deviation(self):

        print("")
        print("Standard deviation: ", self.__st_dev)
        print("")