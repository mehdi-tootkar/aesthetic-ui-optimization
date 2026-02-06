from server.env.aesthetic_env import AestheticUIEnv

env = AestheticUIEnv(
    api_url="http://127.0.0.1:8000/score",
    image_path="ui_test.png",
    n_actions=10,
    max_steps=5
)

obs, info = env.reset()
print("RESET:", obs, info)

for t in range(5):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"STEP {t+1}: action={action} reward={reward:.4f} obs={obs} info={info}")
    if terminated or truncated:
        break
