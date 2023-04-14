from math import sin, cos
from Function import Func
from Func_Values import F_x_
from X_values import X
from Numerical_Integration_Methods import Integral


func = Func(-10, 20, 1, lambda x : x**3 + 3 * x)

values_func = F_x_(-10, 20, 1, lambda x : x**3 + 3 * x)

values_x = X(func)

values_x.double_values(func)

values_x.print_nodes_x()

integral = Integral()

integral.method_left(func.Get_h(), func.Get_n(), values_x.Get_nodes(), values_func)

integral.method_right(func.Get_h(), func.Get_n(), values_x.Get_nodes(), values_func)

integral.method_middle(func.Get_h(), func.Get_n(), values_x.Get_nodes(), values_func)

integral.method_trap(func.Get_h(), func.Get_n(), values_x.Get_nodes(), values_func)

integral.Simpson_formula(func.Get_h(), func.Get_n(), values_x.Get_nodes(), values_func)

integral.print_left_met_rect()

integral.print_right_met_rect()

integral.print_middle_met_rect()

integral.print_trap_met()

integral.print_Sim_met()

integral.deviation(960)

integral.print_deviation()

values_func.print_func_values()