def advanced_hash(data: bytes, seed: int = 0) -> int:
    # Constants inspired by MurmurHash
    m = 0x5bd1e995  # A prime multiplier (common in many hash algorithms)
    r = 24          # A constant for the right shift operation

    length = len(data)
    h = seed ^ length  # Initialize hash with seed and combine with data length
    
    # Process the input in 4-byte (32-bit) blocks
    num_blocks = length // 4
    for i in range(num_blocks):
        # Extract 4 bytes, little-endian
        k = int.from_bytes(data[i*4:(i+1)*4], 'little')
        
        # Mix k: multiply, XOR shift, and multiply again
        k *= m
        k &= 0xFFFFFFFF  # Ensure k remains 32-bit
        k ^= k >> r
        k *= m
        k &= 0xFFFFFFFF  # Again, keep k within 32-bits

        # Mix with hash
        h *= m
        h &= 0xFFFFFFFF
        h ^= k

    # Handle the remaining bytes (if any)
    remaining_bytes = length & 3  # Same as length % 4
    if remaining_bytes:
        remaining_data = data[num_blocks*4:]
        # Combine the remaining bytes into an integer
        rem_int = int.from_bytes(remaining_data + b'\x00'*(4 - remaining_bytes), 'little')
        h ^= rem_int
        h *= m
        h &= 0xFFFFFFFF

    # Final mixing of the hash to ensure a uniform distribution
    h ^= h >> 13
    h *= m
    h &= 0xFFFFFFFF
    h ^= h >> 15

    return h

# Example usage:
if __name__ == "__main__":
    sample_data = b"Advanced hashing with block mixing and bitwise operations"
    print("Hash Value:", advanced_hash(sample_data, seed=42))
