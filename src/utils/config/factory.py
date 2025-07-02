from .ssm_provider import SSMParameterProvider

def get_config_provider():
    # Add logic here to select provider based on environment
    return SSMParameterProvider()