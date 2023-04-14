class Central_Diff_Der:

    __derivatives_func = {}

        
    def derivative(self, value_x, value_func, func):

        for x in value_x.Get_nodes():

            self.__derivatives_func.update( { "f'(" + x + ")" : (value_func.calculation(value_x.Get_nodes()[x] + func.Get_h()) - value_func.calculation(value_x.Get_nodes()[x] - func.Get_h())) // 2 * func.Get_h() } )

    
    def print_derivatives_func(self):

        print("")
        print("Central difference derivative: ", self.__derivatives_func)
        print("")


    def Get_Derivatives_Func(self):

        return self.__derivatives_func