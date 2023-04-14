class Integral:

    __area_left_rect = {}

    __area_right_rect = {}

    __area_middle_rect = {}

    __area_met_trap = {}

    __area_met_Sim = {}

    __deviat = {}


    def method_left(self, h, n, values_x, func_values):

        for i in range(0, n):

            self.__area_left_rect.update( { "f(x" + str(i) + ")" : func_values.calculation(values_x['x' + str(i)]) } )    

        self.__area_left_rect.update( { "I" : h * sum(self.__area_left_rect.values()) } )


    def method_right(self, h, n, values_x, func_values):

        for i in range(1, n + 1):

            self.__area_right_rect.update( { "f(x" + str(i) + ")" : func_values.calculation(values_x['x' + str(i)]) } )

        self.__area_right_rect.update( { "I" : h * sum(self.__area_right_rect.values()) } )


    def method_middle(self, h, n, values_x, func_values):

        for i in range(0, n):

            self.__area_middle_rect.update( { "f(x" + str(i) + ")" : func_values.calculation(values_x['x' + str(i)] + h // 2) } )

        self.__area_middle_rect.update( { "I" : h * sum(self.__area_middle_rect.values()) } )


    def method_trap(self, h, n, values_x, func_values):

        for i in range(1, n):

            self.__area_met_trap.update( { "f(x" + str(i) + ")" : func_values.calculation(values_x['x' + str(i)]) } )

        self.__area_met_trap.update( { "I" : (h // 2) * (func_values.calculation(values_x["x0"]) + 2 * sum(self.__area_met_trap.values()) + func_values.calculation(values_x["x" + str(n)])) } )


    def Simpson_formula(self, h, n, values_x, func_values):

        for i in range(1, 2 * n + 1):

            self.__area_met_Sim.update( { "f(x" + str(i) + ")" : func_values.calculation(values_x['x' + str(i)]) } )

        self.__area_met_Sim.update( { "I" : (h // 3) * (func_values.calculation(values_x["x0"]) + 4 * sum(list(self.__area_met_Sim.values())[::2]) + 2 * sum(list(self.__area_met_Sim.values())[1::2]) + func_values.calculation(values_x["x" + str(2 * n)])) } )


    def deviation(self, true_value):

        self.__deviat.update( { "Left rectangle method " : true_value - self.__area_left_rect["I"] } )

        self.__deviat.update( { "Right rectangle method " : true_value - self.__area_right_rect["I"] } )

        self.__deviat.update( { "Middle rectangle method " : true_value - self.__area_middle_rect["I"] } )

        self.__deviat.update( { "Trapezoidal method " : true_value - self.__area_met_trap["I"] } )

        self.__deviat.update( { "Simpson method " : true_value - self.__area_met_Sim["I"] } )


    def print_left_met_rect(self):

        print("Left rectangle method: ", self.__area_left_rect)
        print("")


    def print_right_met_rect(self):

        print("Right rectangle method: ", self.__area_right_rect)
        print("")


    def print_middle_met_rect(self):

        print("Middle rectangle method: ", self.__area_middle_rect)
        print("")


    def print_trap_met(self):

        print("Trapezoidal method: ", self.__area_met_trap)
        print("")


    def print_Sim_met(self):

        print("Simpson method: ", self.__area_met_Sim)
        print("")


    def print_deviation(self):

        print("Deviation of numerical values from true values: ", self.__deviat)
        print("")
