import os

from django.core.exceptions import ImproperlyConfigured


def get_required_env_value(env_variable_name: str):
    res = os.getenv(env_variable_name)
    if res is None:
        raise ImproperlyConfigured(
            f"Value for env variable '{env_variable_name}' is required."
        )
    return res
