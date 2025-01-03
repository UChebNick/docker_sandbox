import uuid


def generate_random_hex(length):
    return uuid.uuid4().hex[:length]
