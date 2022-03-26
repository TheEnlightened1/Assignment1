"""
Assignment 1
Semester 1, 2022
ENGG1001
"""

# Replace these <strings> with your name, student number and email address.
__author__ = "<Sam Goan>, <45403844>"
__email__ = "<s.goan@uq.net.au>"

HELP = """
'i' - prompt for the input parameters
'd' - determine distances to lift-off for the current input parameters
'p <increments> <step>' - print out a table of distances to lift-off for different drag coefficients
'h' - help message
'q' - quit"""

def prompt_for_inputs():
    '''
    Returns: values: tuple[float, ...], drag˙coeff: float
    The first tuple of floats should contain the following values:
    mass, force, ref˙area, density, init˙velocity, lift˙velocity,
    start˙position, time˙inc
    '''

    values = float(input("Input mass of the plane (in kg): ")), float(input("Input engine force (in N): ")), float(input("Input reference area (in m^2): ")), float(input("Input air density (in kg/m^3): ")), float(input("Input initial velocity at start of runway (in m/s): ")), float(input("Input lift-off velocity (in m/s): ")), float(input("Input position of the start of the runway (in m): ")), float(input("Input time increment (in secs): ")),

    drag_coeff = float(input("Input drag coefficient: "))

    return values, drag_coeff

def compute_trajectory(values, drag_coeff):
    '''
    Parameters:
    values (tuple[float, ...]): mass, force, ref˙area, density,
    init˙velocity, lift˙velocity, start˙position, time˙inc
    drag˙coeff (float): The drag coefficient.
    Returns:
    (tuple[tuple[float, ...], tuple[float, ...]]): The first tuple
    contains the positions (in meters) along the runway for each
    '''

    m = values[0]
    F_thrust = values[1]
    A_ref = values[2]
    p = values[3]
    v0 = values[4]
    v_lift = values[5]
    x0 = values[6]
    t_i = values[7]

    velocities = []

    positions = []

    velocity = v0

    while velocity < v_lift:
        accel = 1/m * (F_thrust - 0.5 * p * velocity**2 * A_ref * drag_coeff)
        position = x0 + velocity*(t_i) + 0.5 * accel * (t_i**2)
        x0 = position
        position = round(position, 3)
        positions.append(position)
        velocity = velocity + (accel * t_i)
        velocity = round(velocity, 3)
        velocities.append(velocity)

    return tuple(positions), tuple(velocities)



def print_table(values, drag_coeff, increments, step):

    '''
    Parameters:
    values (tuple[float, ...]): mass, force, ref˙area, density,
    init˙velocity, lift˙velocity, start˙position, time˙inc
    drag˙coeff (float): The drag coefficient.
    increments (int): The number of drag coefficients displayed.
    step (float): The difference between each drag coefficient.
    Returns:
    None
    '''

    new_drag = drag_coeff

    print('**************************************')
    print('* Drag coefficient * Runway distance *')
    print('**************************************' )


    for i in range(0, increments):
        new_val = compute_trajectory(values, new_drag)
        last_val = new_val[0][-1:][0]
        new_drag = round(new_drag, 4)
        print(('*{:^18}*{:^17}*'.format(new_drag, last_val)))
        new_drag += step

    print('**************************************\n')



def main():
    """Entry point to interaction"""
    #print("Implement your solution and run this file")

    while True:

        input_var = input("Please enter a command: ")

        input_var = input_var.split(" ")

        if input_var[0] == "i":
            values, drag_coeff = prompt_for_inputs()
        elif input_var[0] == "p":
            try:
                print(print_table(values, drag_coeff, int(input_var[1]), float(input_var[2])))
            except:
                print("Please enter the parameters first.")
        elif input_var[0] == 'h':
            print(HELP)
        elif input_var[0] == 'q':
            q_var = input("Are you sure (y/n): ")
            if q_var == 'y':
                break

def bonus(values, runway_distance):

    '''
    Parameters:
        values (tuple[float, ...]): mass, force, ref˙area, density,
            init˙velocity, lift˙velocity, start˙position, time˙inc
        runway˙distance (float): The runway distance.

    Returns:
        None
    '''

    x0 = values[6]

    drag_coeff = 0

    step = 0.00001

    while x0 <= runway_distance:
        new_val = compute_trajectory(values, drag_coeff)
        x0 = new_val[0][-1:][0]
        drag_coeff += step
        x0 += x0
    return drag_coeff


if __name__ == "__main__":
    main()
    pass

#print(bonus((50000, 600000, 800, 1, 0, 70, 0, 0.1), 1500))
