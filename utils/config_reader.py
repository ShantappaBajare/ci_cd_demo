import json
import os

ENV = os.environ.get("ENV", "local")  # "local" or "ci"

config_file = "config_local.json" if ENV.lower() == "local" else "config_local.json"

config_path = os.path.join(
    os.path.dirname(__file__),
    "../config",
    config_file
)

def read_config():
    with open(config_path) as f:
        return json.load(f)