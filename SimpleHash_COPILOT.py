def simple_hash(s):
    hash_val = 0
    # A constant prime multiplier (31 is common in many string hash functions)
    multiplier = 31
    mod_value = 10**9 + 7  # A large prime to reduce collisions via modulo arithmetic
    
    for char in s:
        # Multiply to shift and add the ordinal value of the character
        hash_val = (hash_val * multiplier + ord(char)) % mod_value
    return hash_val

# Testing the hash function
print(simple_hash("Hello, world!"))
