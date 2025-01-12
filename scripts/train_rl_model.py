from stable_baselines3 import PPO
from stable_baselines3.common.envs import DummyVecEnv
from chatbot_env import ChatbotEnv

env = DummyVecEnv([lambda: ChatbotEnv()])
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)
model.save("adaptive_chatbot_model")
