import random
from utils.cfg import CONFIG
import bcrypt
import vk

token = CONFIG.VK_TOCKEN


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


def check_password(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())