from Function import Func

class X(Func):

    __nodes_x = {}


    def __init__(self, func):
        
        for i in range(0, func.Get_n() + 1):
            
            self.__nodes_x.update( { 'x' + str(i) : func.Get_a() + func.Get_h() * i } )


    def double_values(self, func):

        for i in range(func.Get_n() + 1, 2 * func.Get_n() + 1):

            self.__nodes_x.update( { 'x' + str(i) : func.Get_a() + func.Get_h() * i } )


    def Get_nodes(self):

        return self.__nodes_x
    

    def print_nodes_x(self):

        print("")
        print("Nodes: ", self.__nodes_x)
        print("")