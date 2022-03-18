m = 50000
F_thrust = 600000
A_ref = 800
p = 1
v0 =0
v_lift = 70
x0 = 0
t_i = 0.1
drag_coeff = 0.015
drag_coeff1 = 0.045
drag_coeff2 = 0.075
drag_coeff3 = 0.105
drag_coeff4 = 0.135





a_i = 1/m * (F_thrust - (0.5 * p * 1.2**2 * A_ref * drag_coeff3))

position = x0 + (1.2*0.1) + 0.5 * a_i * (t_i**2)

round_3 = round(a_i, 3)

print(a_i)
#
# print(round_3)

print(position)
