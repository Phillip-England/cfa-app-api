import bcrypt


def hash_string(string: str):
    salt = bcrypt.gensalt()
    string_bytes = string.encode()
    return bcrypt.hashpw(string_bytes, salt).decode('utf-8')


def compare_hash(string: str, hashed_string: str):
    hash_matches = bcrypt.checkpw(string.encode(
        'utf-8'), hashed_string.encode('utf-8'))
    if hash_matches != True:
        return Exception('compared hash values do not match')
