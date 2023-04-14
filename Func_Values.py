from Function import Func

class F_x_(Func):

    __func_values = {}


    def __init__(self, a, b, h, function):
        
        super().__init__(a, b, h, function)


    def calculation(self, x):

        if ("f(" + str(x) + ")") not in self.__func_values.keys():

            result = self.func(x)

            self.__func_values.update( { 'f(' + str(x) + ')' : result } )

            return self.__func_values["f(" + str(x) + ")"]

        else:

            return self.__func_values["f(" + str(x) + ")"]
        
    
    def Get_func_values(self):

        return self.__func_values
    

    def print_func_values(self):

        print("")
        print("Function values: ", self.__func_values)
        print("")