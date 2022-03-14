'''this is a drafts file'''


def prompt_for_inputs(): #-> tuple[tuple[float, ...], float]:
    """
Returns: values: tuple[float, ...], drag˙coeff: float

The first tuple of floats should contain the following values:
mass, force, ref˙area, density, init˙velocity, lift˙velocity, start˙position, time˙inc
    """
    #values = ()

    values = float(input("Input mass of plane: ")), float(input("Input engine force (in N): ")), float(input("Input reference area (in mˆ2): ")), \
    float(input("Input air density (in kg/mˆ3): ")), float(input("Input initial velocity at start of runway (in m/s): ")), \
    float(input("Input lift-off velocity (in m/s): ")), float(input("Input position of the start of the runway (in m): ")), \
    float(input("Input time increment (in secs):  ")),

    drag_coeff = float(input("Input drag coefficient:   "))
    #breakpoint()

    return values, drag_coeff

def compute_trajectory(values, drag_coeff):
#def compute_trajectory():

    m = values[0]
    F_thrust = values[1]
    A_ref = values[2]
    p = values[3]
    v0 = values[4]
    v_lift = values[5]
    x0 = values[6]
    t_i = values[7]

    # m = 50000
    # F_thrust = 600000
    # A_ref = 800
    # p = 1
    # v0 = 2
    # v_lift = 70
    # x0 = 0
    # t_i = 0.1
    # drag_coeff = 0.015
    # # #breakpoint()
    a_i = 1/m * (F_thrust - 0.5 * p * v0**2 * A_ref * drag_coeff)

    velocities = []

    positions = []

    time_delta = 0

    velocity = v0 + (a_i*time_delta)

    # velocity_full = ()

    breakpoint()
    while velocity < v_lift:

        time_delta += t_i
        velocity = v0 + (a_i*time_delta)
        format.round(velocity, 3)
        #breakpoint()
        velocities.append(velocity)
        position = x0 + velocity * time_delta + 0.5 * a_i * (time_delta**2)
        position += position
        round(position, 3)
        positions.append(position)


    return tuple(velocities), tuple(positions)
 ###Printing values for velocity and position fine but I need to return them as a tuple of the results

######################################
######################################
# print(prompt_for_inputs())
values, drag_coeff = prompt_for_inputs()

#velocities, positions = compute_trajectory()

print(compute_trajectory(values, drag_coeff))



# print(velocities)
