import json
import os

def read_config():

    config_path = os.path.join(
        os.path.dirname(__file__),
        "../config/config.json"
    )

    with open(config_path) as f:
        config = json.load(f)

    return config