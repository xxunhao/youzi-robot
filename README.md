# youzi-robot

[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

`youzi-robot` provides Gymnasium environments for simulated applications of the Low Cost Robot platform.
This project is adapted from the original gym-lowcostrobot repository.

## Installation

```bash
pip install youzi-robot
```

## Usage

```python
import gymnasium as gym
import youzi_robot

env = gym.make("PickPlaceCube-v0", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

## Available Environments

- `LiftCube-v0`
- `PickPlaceCube-v0`
- `PushCube-v0`
- `ReachCube-v0`
- `StackTwoCubes-v0`
- `PushCubeLoop-v0`

## Headless Mode

```sh
export MUJOCO_GL=osmesa
export DISPLAY=:0
```

## Training with RL Zoo3

```sh
python -u -m rl_zoo3.train --algo tqc --env ReachCube-v0 --gym-packages youzi_robot -conf examples/rl_zoo3_conf.yaml --env-kwargs observation_mode:'"both"' -f logs
```

## Development

```sh
ruff format youzi_robot examples tests setup.py --line-length 127
pytest
```

## Build & Publish

```sh
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

## Project Links

- Homepage: https://github.com/xxunhao/youzi-robot
- Repository: https://github.com/xxunhao/youzi-robot
- Issues: https://github.com/xxunhao/youzi-robot/issues

## License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE).
