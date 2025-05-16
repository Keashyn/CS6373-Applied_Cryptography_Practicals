import string
from collections import Counter

def convert_hex_to_bytes(hex_string):
    """Convert a hexadecimal  string into a byte array."""
    return bytes.fromhex(hex_string)

def decrypt_with_xor(ciphertext, key):
    """Decrypt any ciphertext with XOR using the provided key."""
    return bytes(c ^ key[i % len(key)] for i, c in enumerate(ciphertext))

def find_optimal_key_length(ciphertext):
    """Determine the most likely  key length based on repeating patterns."""
    optimal_length = 1
    highest_score = 0
    for length in range(1, 14):  # Check  key lengths from  (1 to 13)
        segments = [ciphertext[i::length] for i in range(length)]
        score = sum(Counter(segment).most_common(1)[0][1] for segment in segments)
        if score > highest_score:
            optimal_length, highest_score = length, score
    return optimal_length

def deduce_key(ciphertext, key_length):
    """Attempt to deduce the encryption key by using frequency analysis on each key position."""
    key = bytearray(key_length)
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        best_score = 0
        best_byte = 0
        for candidate in range(256):  # Try all possible byte values (0-255)
            decrypted_segment = bytes(c ^ candidate for c in segment)
            score = sum(decrypted_segment.count(letter) for letter in "etaoinshrdlcumwfgypbvkjxqz ".encode())
            if score > best_score:
                best_byte, best_score = candidate, score
        key[i] = best_byte
    return key

def run_decryption():
    # Prompt user for the ciphertext input
    print("Please enter the ciphertext in hexadecimal format (you can enter multiple lines). Press Enter twice to finish:")
    hex_input = ""
    while True:
        line = input()
        if line == "":
            break
        hex_input += line.strip().replace(" ", "")

    # Validate the input to ensure it is a valid hex string
    if not all(char in string.hexdigits for char in hex_input):
        print("Error: The input contains invalid non-hexadecimal characters.")
        return

    # Convert the hex string to bytes
    try:
        ciphertext = convert_hex_to_bytes(hex_input)
    except ValueError as e:
        print(f"Error converting hex to bytes: {e}")
        return

    # Step 1: Estimate  the key length
    estimated_length = find_optimal_key_length(ciphertext)
    print(f"Estimated Key Length: {estimated_length}")

    # Step 2: Recover the key
    recovered_key = deduce_key(ciphertext, estimated_length)
    print(f"Recovered Key: {recovered_key.hex()}")

    # Step 3: Decrypt the ciphertext
    plaintext = decrypt_with_xor(ciphertext, recovered_key)
    print("\nRecovered Plaintext:\n")
    print(plaintext.decode(errors="ignore"))  # Ignore errors for non-printable bytes

if __name__ == "__main__":
    run_decryption()