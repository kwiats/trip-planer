import random
import base64


def generate_otp():
    number = random.randrange(1, 1000000)
    return str(number).zfill(6)

def convert_to_base64(number: str):
    bytes_data = number.encode('utf-8')
    return base64.b32encode(bytes_data).decode('utf-8').rstrip('=')