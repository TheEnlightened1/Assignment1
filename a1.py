"""
Assignment 1
Semester 1, 2022
ENGG1001
"""

# Replace these <strings> with your name, student number and email address.
__author__ = "<Your Name>, <Your Student Number>"
__email__ = "<Your Student Email>"

HELP = """
    'i' - prompt for the input parameters
    'd' - determine distances to lift-off for the current input parameters
    'p <increments> <step>' - print out a table of distances to lift-off for different drag coefficients
    'h' - help message
    'q' - quit
"""

def prompt_for_inputs() -> tuple[tuple[float, ...], float]:
    values = float(input("Input mass of the plane (in kg): ")), float(input("Input engine force (in N): ")), float(input("Input reference area (in m^2): ")), float(input("Input air density (in kg/m^3): ")), float(input("Input initial velocity at start of runway (in m/s): ")), float(input("Input lift-off velocity (in m/s): ")), float(input("Input position of the start of the runway (in m): ")), float(input("Input time increment (in secs): ")),

    drag_coeff = float(input("Input drag coefficient: "))

    return values, drag_coeff

def compute_trajectory(values: tuple[float, ...],
        drag_coeff: float) -> tuple[tuple[float, ...], tuple[float, ...]]:
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



def print_table(values: tuple[float, ...], drag_coeff: float, increments: int, step: float):

    new_drag = drag_coeff

    print('**************************************')
    print('* Drag coefficient * Runway distance *')
    print('**************************************')


    for i in range(0, increments):
        new_val = compute_trajectory(values, new_drag)
        last_val = new_val[0][-1:][0]
        new_drag = round(new_drag, 4)
        print(('*     {}        *     {}     *'.format(new_drag, last_val)))
        new_drag += step

    print('**************************************')


def main():
    """Entry point to interaction"""
    print("Implement your solution and run this file")
    pass

if __name__ == "__main__":
    main()
    pass
