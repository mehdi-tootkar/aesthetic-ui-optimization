import gymnasium as gym
from gymnasium import spaces
import numpy as np
import requests
from pathlib import Path


class AestheticUIEnv(gym.Env):
    """
    Minimal Gymnasium environment that uses an external FastAPI aesthetic scorer.

    Observation (for MVP): a small numeric vector (e.g., last score, step ratio)
    Action (for MVP): discrete actions (placeholder now)
    Reward: delta aesthetic score (new_score - old_score)
    """

    metadata = {"render_modes": []}

    def __init__(
        self,
        api_url: str = "http://127.0.0.1:8000/score",
        image_path: str = "ui_test.png",
        n_actions: int = 10,
        max_steps: int = 20,
        timeout_s: float = 60.0,
    ):
        super().__init__()
        self.api_url = api_url
        self.image_path = Path(image_path)
        self.n_actions = n_actions
        self.max_steps = max_steps
        self.timeout_s = timeout_s

        # Discrete action space (later: real actions sent to Figma)
        self.action_space = spaces.Discrete(self.n_actions)

        # Minimal observation: [last_score, step_fraction]
        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0], dtype=np.float32),
            high=np.array([10.0, 1.0], dtype=np.float32),
            dtype=np.float32,
        )

        self._step_count = 0
        self._prev_score = None

    def _score_image_via_api(self, image_bytes: bytes) -> float:
        payload = {"image": list(image_bytes)}
        r = requests.post(self.api_url, json=payload, timeout=self.timeout_s)
        r.raise_for_status()
        return float(r.json()["score"])

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self._step_count = 0

        # For MVP we always start from the same image.
        # Later: reset will instruct Figma to restore baseline UI and export fresh image.
        img_bytes = self.image_path.read_bytes()
        score = self._score_image_via_api(img_bytes)

        self._prev_score = score

        obs = np.array([score, 0.0], dtype=np.float32)
        info = {"score": score}

        return obs, info

    def step(self, action):
        self._step_count += 1

        # MVP: action does not change the image yet (placeholder).
        # Later: action will be sent to Figma to modify UI, then export a new image.
        img_bytes = self.image_path.read_bytes()
        new_score = self._score_image_via_api(img_bytes)

        reward = new_score - float(self._prev_score)
        self._prev_score = new_score

        terminated = False  # no terminal state in MVP
        truncated = self._step_count >= self.max_steps

        obs = np.array(
            [new_score, self._step_count / self.max_steps],
            dtype=np.float32
        )
        info = {"score": new_score, "action": int(action)}

        return obs, float(reward), terminated, truncated, info
