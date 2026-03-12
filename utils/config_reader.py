# utils/config_reader.py
import json
import os

def read_config():
    """
    Reads the configuration based on the ENV variable.
    Defaults to 'local' if ENV is not set.
    """
    ENV = os.environ.get("ENV", "local").lower()  # local / ci / docker / github / jenkins

    # Determine config file path
    config_filename = "config.json"  # default
    if ENV in ["ci", "docker", "github", "jenkins"]:
        config_filename = "config_ci.json"  # you can maintain a separate config if needed

    config_path = os.path.join(
        os.path.dirname(__file__),
        "../config",
        config_filename
    )

    # Load the config file
    with open(config_path) as f:
        config = json.load(f)

    # Optionally override some settings via ENV variables (e.g., base_url)
    config["base_url"] = os.environ.get("BASE_URL", config.get("base_url"))
    config["username"] = os.environ.get("USERNAME", config.get("username"))
    config["password"] = os.environ.get("PASSWORD", config.get("password"))
    config["browser"] = os.environ.get("BROWSER", config.get("browser"))

    return config