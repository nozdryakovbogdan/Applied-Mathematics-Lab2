class True_Derivative_Values:

    __true_values = {}


    derivative = lambda : 'derivative'


    def __init__(self, derivative):

        self.derivative = derivative

    
    def true_derivative(self, x_values):

        for x in x_values.Get_nodes():

            self.__true_values.update( { "f'(" + x + ")" : self.derivative(x_values.Get_nodes()[x])} )

        
    def print_true_der(self):

        print("True values of the derivative: ", self.__true_values)


    def Get_True_Values(self):

        return self.__true_values  