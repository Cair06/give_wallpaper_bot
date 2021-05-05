import random, os
API_TOKEN = ''

def random_file(path):
    random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
    return random_filename
