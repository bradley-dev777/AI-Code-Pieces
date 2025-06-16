def simple_hash(text, seed=31):
    hash_value = 0
    for char in text:
        hash_value = (hash_value * seed + ord(char)) % (2**32)
    return hash_value
