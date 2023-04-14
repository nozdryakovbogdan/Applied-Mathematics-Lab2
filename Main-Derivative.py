from math import sin, cos
from Function import Func
from Func_Values import F_x_
from X_values import X
from Rigt_diff_der_alg import Right_Diff_Der
from Left_diff_der_alg import Left_Diff_Der
from Central_diff_der_alg import Central_Diff_Der
from True_Values import True_Derivative_Values
from Mathematical_Parameters import Mat_Par


func = Func(-16, 16, 1, lambda x : x ** 2 + 14)

values_func = F_x_(-16, 16, 1, lambda x : x ** 2 + 14)

values_x = X(func)

values_x.print_nodes_x()

alg1 = Right_Diff_Der()

alg1.derivative(values_x, values_func, func)

alg1.print_derivatives_func()

alg2 = Left_Diff_Der()

alg2.derivative(values_x, values_func, func)

alg2.print_derivatives_func()

alg3 = Central_Diff_Der()

alg3.derivative(values_x, values_func, func)

alg3.print_derivatives_func()

values_func.print_func_values()

true_der = True_Derivative_Values(lambda x : 2 * x)

true_der.true_derivative(values_x)

true_der.print_true_der()

mat_par = Mat_Par()

print("")
print("Right difference derivative:")
print("")


mat_par.average_value(alg1.Get_Derivatives_Func())

mat_par.print_average_value()

mat_par.deviation(true_der.Get_True_Values())

mat_par.print_deviation()

mat_par.dispersion()

mat_par.print_dispersion()

mat_par.standard_deviation()

mat_par.print_standard_deviation()

print("")
print("Left difference derivative:")
print("")

mat_par.average_value(alg2.Get_Derivatives_Func())

mat_par.print_average_value()

mat_par.deviation(true_der.Get_True_Values())

mat_par.print_deviation()

mat_par.dispersion()

mat_par.print_dispersion()

mat_par.standard_deviation()

mat_par.print_standard_deviation()

print("")
print("Central difference derivative:")
print("")

mat_par.average_value(alg3.Get_Derivatives_Func())

mat_par.print_average_value()

mat_par.deviation(true_der.Get_True_Values())

mat_par.print_deviation()

mat_par.dispersion()

mat_par.print_dispersion()

mat_par.standard_deviation()

mat_par.print_standard_deviation()