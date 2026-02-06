import random

class DummyAgent:
    def __init__(self, action_space_size: int):
        self.n_actions = action_space_size

    def act(self, state):
        action_id = random.randint(0, self.n_actions - 1)
        target = random.choice(state.elements)
        return {
            "action_id": action_id,
            "target_id": target.id,
            "params": {"delta": 0.02}
        }
