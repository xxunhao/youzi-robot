import os

from gymnasium.envs.registration import register

__version__ = "0.1.0"

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets", "low_cost_robot_6dof")

register(
    id="LiftCube-v0",
    entry_point="youzi_robot.envs:LiftCubeEnv",
    max_episode_steps=50,
    nondeterministic=True,
)

register(
    id="PickPlaceCube-v0",
    entry_point="youzi_robot.envs:PickPlaceCubeEnv",
    max_episode_steps=50,
    nondeterministic=True,
)

register(
    id="PushCube-v0",
    entry_point="youzi_robot.envs:PushCubeEnv",
    max_episode_steps=50,
    nondeterministic=True,
)

register(
    id="ReachCube-v0",
    entry_point="youzi_robot.envs:ReachCubeEnv",
    max_episode_steps=50,
    nondeterministic=True,
)

register(
    id="StackTwoCubes-v0",
    entry_point="youzi_robot.envs:StackTwoCubesEnv",
    max_episode_steps=50,
    nondeterministic=True,
)

register(
    id="PushCubeLoop-v0",
    entry_point="youzi_robot.envs:PushCubeLoopEnv",
    max_episode_steps=50,
    nondeterministic=True,
)
