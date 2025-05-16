import sys

def is_valid_ascii(byte):
    """Check if the byte corresponds to a valid ASCII character or null."""
    return (65 <= byte <= 90) or (97 <= byte <= 122) or (byte == 0)


def xor_bytes(byte_str1, byte_str2):
    """XOR two byte strings, padding the shorter one with null bytes."""
    return bytes(a ^ b for a, b in zip(byte_str1, byte_str2.ljust(len(byte_str1), b'\0')))


def validate_hex_input(hex_string):
    """Check if the input string is a valid hexadecimal string."""
    try:
        bytes.fromhex(hex_string)
        return True
    except ValueError:
        return False


def save_decrypted_messages(decrypted_messages):
    """Save decrypted messages to a text file."""
    with open("decrypted_messages.txt", "w") as f:
        for index, message in enumerate(decrypted_messages):
            f.write(f"{index + 1}: {message}\n")
    print("Decrypted messages saved to 'decrypted_messages.txt'.")


def main():
    # Prompt user for encrypted messages in hexadecimal format
    encrypted_messages = []
    print("Enter your encrypted messages (you can enter multiple lines). Press Enter twice to finish:")

    while True:
        line = input()
        if line.lower() == "":
            break
        if validate_hex_input(line.strip()):
            encrypted_messages.append(line.strip())
        else:
            print("Invalid hexadecimal input. Please try again.")

    # Decode hex messages to bytes
    decoded_messages = [bytes.fromhex(msg) for msg in encrypted_messages]

    # Dictionary to hold the stream cipher values
    cipher_stream = {}

    # Analyze each message to find potential spaces
    for index in range(len(decoded_messages)):
        frequency_dict = {}

        for compare_index in range(len(decoded_messages)):
            if compare_index == index:
                continue

            xor_result = xor_bytes(decoded_messages[index], decoded_messages[compare_index])

            for position in range(len(xor_result)):
                if is_valid_ascii(xor_result[position]):
                    frequency_dict[position] = frequency_dict.get(position, 0) + 1

        print(f"\nPossible spaces in message {index + 1}:")
        for key in list(frequency_dict.keys()):
            if frequency_dict[key] < len(encrypted_messages) - 2:
                del frequency_dict[key]

        print(frequency_dict)
        print(f"Possible key bytes from message {index + 1}:")

        for key in frequency_dict.keys():
            stream_value = decoded_messages[index][key] ^ ord(" ")
            print(f"cipher_stream[{key}] = {stream_value}")
            cipher_stream[key] = stream_value

    # Manual adjustments to the cipher stream
    cipher_stream[0] = decoded_messages[0][0] ^ ord('I')
    cipher_stream[6] = decoded_messages[5][6] ^ ord('s')
    cipher_stream[8] = decoded_messages[0][8] ^ ord('n')
    cipher_stream[10] = decoded_messages[0][10] ^ ord('i')
    cipher_stream[17] = decoded_messages[0][17] ^ ord('e')
    cipher_stream[20] = decoded_messages[0][20] ^ ord('e')
    cipher_stream[29] = decoded_messages[0][29] ^ ord('n')
    cipher_stream[30] = decoded_messages[3][30] ^ ord('?')

    # Decrypt the messages using the constructed cipher stream
    print("\nDecrypted Messages:")
    decrypted_messages = []
    for index, msg in enumerate(encrypted_messages):
        decrypted_message = bytes.fromhex(msg)
        decrypted_chars = bytearray(decrypted_message)

        for i in range(len(decrypted_chars)):
            if i in cipher_stream:
                decrypted_chars[i] ^= cipher_stream[i]

        # Display the decrypted message
        plaintext = "".join(chr(c) for c in decrypted_chars)
        decrypted_messages.append(plaintext)
        print(f"{index + 1}: {plaintext}")

    # Option to save decrypted messages
    save_option = input("\nWould you like to save the decrypted messages to a file? (y/n): ")
    if save_option.lower() == 'y':
        save_decrypted_messages(decrypted_messages)

if __name__ == "__main__":
    main()