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
    breakpoint()

    return values, drag_coeff

print(prompt_for_inputs())
