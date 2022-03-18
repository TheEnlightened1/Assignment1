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
    values = float(input("Input mass of plane: ")), float(input("Input engine force (in N): ")), float(input("Input reference area (in mˆ2): ")), \
    float(input("Input air density (in kg/mˆ3): ")), float(input("Input initial velocity at start of runway (in m/s): ")), \
    float(input("Input lift-off velocity (in m/s): ")), float(input("Input position of the start of the runway (in m): ")), \
    float(input("Input time increment (in secs):  ")),

    drag_coeff = float(input("Input drag coefficient:   "))

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

    a_i = 1/m * (F_thrust - 0.5 * p * v0**2 * A_ref * drag_coeff)

    velocities = []

    positions = []

    time_delta = 0

    velocity = v0 + (a_i*t_i)

    position1 = 0

    while velocity < v_lift:
        accel = 1/m * (F_thrust - 0.5 * p * velocity**2 * A_ref * drag_coeff)
        time_delta += t_i
        velocity = v0 + (accel * time_delta)
        velocity = round(velocity, 3)
        velocities.append(velocity)
        position =  0.5 * accel * (time_delta**2)
        position = round(position, 3)
        positions.append(position)

    return tuple(velocities), tuple(positions)



def print_table(values: tuple[float, ...], drag_coeff: float, increments: int, step: float):

    new_drag = drag_coeff

    for i in range(0, increments):
        new_val = compute_trajectory(values, new_drag)
        last_val = new_val[1][-1:][0]
        print(last_val)
        new_drag += step

    return


def main():
    """Entry point to interaction"""
    print("Implement your solution and run this file")

if __name__ == "__main__":
    main()
