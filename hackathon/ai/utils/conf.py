from dotenv import load_dotenv

import environ

load_dotenv()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

API_KEY = env('API_KEY')
print(API_KEY)
