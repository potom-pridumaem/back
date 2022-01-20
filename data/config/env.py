from environs import Env

env = Env()
env.read_env()

DATABASE_URL = env.str("DATABASE_URL")
JWT_SECRET = env.str("JWT_SECRET")
