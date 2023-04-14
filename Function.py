class Func:
    
    __a, __b, __h, __n = None, None, None, None


    func = lambda : 'function'


    def __init__(self, a, b, h, function):

        self.__a = a
        self.__b = b
        self.__h = h

        self.__n = (self.__b - self.__a) // self.__h

        self.func = function
    

    def Get_h(self):

        return self.__h
    

    def Get_n(self):

        return self.__n
    

    def Get_a(self):

        return self.__a