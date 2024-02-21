import os

from dotenv import dotenv_values


def load_config():
    """
    Need this, allows safer value loading, defaults, safe panicking, keeps code dry, etc.

    :return: dict
    """
    env_config = dict()

    env_config["ENVIRONMENT"] = os.environ.get("ENVIRONMENT", "development")

    env_config = {
        **env_config,
        **os.environ,  # override loaded values with environment variables
        **dotenv_values("../../.env.shared"),  # load shared development variables
    }

    if env_config["ENVIRONMENT"] == "development":
        env_config = {
            **env_config,
            **dotenv_values("../../.env.secret"),  # load sensitive variables
            **dotenv_values("../../.env.development"),  # load shared development variables
        }
    elif env_config["ENVIRONMENT"] == "production":
        env_config = {
            **env_config,
            **dotenv_values("../../.env.secret"),  # load sensitive variables
            **dotenv_values("../../.env.production"),  # load shared production variables
        }

    return env_config


def test_load_config():
    test_config = load_config()

    assert test_config["ENVIRONMENT"] == "development"
