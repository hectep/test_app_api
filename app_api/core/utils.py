from django.utils.crypto import get_random_string


API_KEY_STRING_LENGTH = 10


def generate_api_key():
    """
    A function to generate api key
    """
    return get_random_string(length=API_KEY_STRING_LENGTH)
