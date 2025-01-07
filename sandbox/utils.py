import os

def generate_random_hex(length):
    num_bytes = (length + 1) // 2
    random_bytes = os.urandom(num_bytes)
    return random_bytes.hex()[:length]
