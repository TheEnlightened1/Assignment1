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

def compute_trajectory(values: tuple[float, ...], drag_coeff: float):
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
    # v0 = 0
    # v_lift = 70
    # x0 = 0
    # t_i = 0.1
    # drag_coeff = 0.015
    # breakpoint()
    a_i = 1/m * (F_thrust - 0.5 * p * v0**2 * A_ref * drag_coeff)
    # round(a_i, 3)
    ##Problems here with Acceleration. With v0, the initial velocity will be 0 which nullifies the drag area, but it keeps
    ##computing that as 0 so all our drag values are wrong. we should actually have two a_i values, one for initial and one that
    ##is constantly updated with new velocity. Or maybe a better way. Try with two accelerations to get functional, refactor later.


    velocities = []

    positions = []

    time_delta = 0

    velocity = v0 + (a_i*t_i)
    # round(velocity, 3)
    position1 = 0
    # velocity_full = ()

    #breakpoint()
    while velocity < v_lift:
        accel = 1/m * (F_thrust - 0.5 * p * velocity**2 * A_ref * drag_coeff) #NOT
        time_delta += t_i
        velocity = v0 + (accel * time_delta) #NOT
        velocity = round(velocity, 3)
        velocities.append(velocity)
        #breakpoint()
        position =  0.5 * accel * (time_delta**2) ##THIS NOW WORKS - WTF, WHAT ABOUT VELOCITY? Matches task sheet, starts to go a little off at
                                                  ##15 values in (13.462) compared to task sheet. Out by 5 at the end but incrementing correct all the way

        position = round(position, 3)
        positions.append(position)
        #breakpoint()


    return tuple(velocities), tuple(positions)

def print_table(increments, step):
#def print_table(values, drag_coeff):
    # m = values[0]
    # F_thrust = values[1]
    # A_ref = values[2]
    # p = values[3]
    # v0 = values[4]
    # v_lift = values[5]
    # x0 = values[6]
    # t_i = values[7]

    # m = 50000
    # F_thrust = 600000
    # A_ref = 800
    # p = 1
    # v0 = 0
    # v_lift = 70
    # x0 = 0
    # t_i = 0.1
    #drag_coeff = 0.015

    new_drag = drag_coeff

    # time_delta = 0

    # position = 0

    # new_drag = 0

    # velocity = 0

    for i in range(0, increments):  ##Appears to be going up, then coming back down through the middle.
        new_val = compute_trajectory(values, new_drag)
        last_val = new_val[1][-1:][0]
        print(('*     {}     *     {}     *'.format(new_drag, last_val)))
        #breakpoint()
        new_drag += step

    return

    # #breakpoint()
    # for i in range(0, increments):
    #     #print(('*     {}     *     {}     *'.format(drag_coeff, position)))
    #     drag_coeff += step
    #     velocity = 0
    #     while velocity < v_lift:
    #         time_delta += t_i
    #         a_i = 1/m * (F_thrust - 0.5 * p * v0**2 * A_ref * drag_coeff)
    #         velocity = v0 + (a_i*time_delta)
    #         position = x0 + velocity * time_delta + 0.5 * a_i * (time_delta**2)

######################################
#   THERE ARE 62 ELEMNTS IN VELOCITY TUPLE
# Positions in task sheet moving from 0.3 to 0.5 to 1, to 2, to 3
# With position = x0 + (velocity*time_delta) + 0.5 * accel * (time_delta**2) moving in much bigger steps, that thats not update position
## ALL NOW WORKING, LOOK AT GETTING PRINT TABLE RIGHT THEN MOVE TO MAIN - PRINT TABLE ALMOST FULLY WORKING
######################################
# print(prompt_for_inputs())
values, drag_coeff = prompt_for_inputs()

velocities, positions = compute_trajectory(values, drag_coeff)

print(compute_trajectory(values, drag_coeff))


# print(print_table(values, drag_coeff, 10, 0.03))

print(print_table(10, 0.03))

#print(len(velocities))



#print(velocities)
