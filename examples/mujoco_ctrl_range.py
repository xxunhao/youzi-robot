import os

import mujoco
from youzi_robot import ASSETS_PATH

if __name__ == "__main__":
    # Load the model from the XML file
    model = mujoco.MjModel.from_xml_path(os.path.join(ASSETS_PATH, "reach_cube.xml"))

    # Extract control range for each actuator
    control_ranges = model.actuator_ctrlrange
    print(type(control_ranges))

    # Print the control ranges
    for i, (lower, upper) in enumerate(control_ranges):
        print(f"Actuator {i} control range: lower = {lower}, upper = {upper}")
