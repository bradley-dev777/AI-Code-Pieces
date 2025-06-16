def advanced_hash(text, seed=0x811c9dc5):
    hash_value = seed
    prime = 0x01000193  # 16777619

    for char in text:
        hash_value ^= ord(char)
        hash_value = (hash_value * prime) & 0xFFFFFFFF  # keep 32-bit
        hash_value ^= (hash_value >> 13)
        hash_value = (hash_value * prime) & 0xFFFFFFFF
        hash_value ^= (hash_value >> 15)

    return hash_value
