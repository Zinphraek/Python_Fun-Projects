import string

# RSA Parameters
p = 3
q = 11
n = p * q  # 33
e = 3  # public exponent
d = 7  # private exponent

lowercase_alphabet = string.ascii_lowercase


def encrypt_char(plain_char):
    """Encrypt a single character"""
    if plain_char == ' ':
        # Space maps to 32
        num = 32
    else:
        # Letters: 'a'=0, 'b'=1, ..., 'z'=25, then add 1 to get 1-26
        num = lowercase_alphabet.index(plain_char.lower()) + 1

    # RSA encryption: (message^e) mod n
    encrypted = (num ** e) % n
    return encrypted


def decrypt_char(cipher_char):
    """Decrypt a single character"""
    # RSA decryption: (cipher^d) mod n
    char = (cipher_char ** d) % n
    return char if char == 32 else (char - 1)


def encrypt_text(plain_text):
    """Encrypt entire text"""
    encrypted_numbers = []
    for char in plain_text:
        encrypted_num = encrypt_char(char)
        encrypted_numbers.append(str(encrypted_num) if encrypted_num > 9 else f"0{encrypted_num}")

    cipher_text = " ".join(encrypted_numbers)
    print(f"Original: {plain_text}")
    print(f"Encrypted: {cipher_text}")
    return cipher_text


def decrypt_text(cipher_text):
    """Decrypt entire text"""
    secret_message = ""
    for cipher in cipher_text.split(" "):
        num = decrypt_char(int(cipher))

        if num == 32:
            secret_message += " "
        elif 0 <= num <= 25:
            secret_message += lowercase_alphabet[num]
        else:
            print(f"Warning: Invalid character index {num}")
            secret_message += "?"  # placeholder for invalid characters

    print(f"Decrypted: {secret_message}")
    return secret_message


def test_rsa():
    """Test the RSA implementation"""
    test_message = "writing proofs"
    print("=== Testing RSA Encryption/Decryption ===")

    # Encrypt
    cipher = encrypt_text(test_message)

    # Decrypt
    decrypted = decrypt_text(cipher)

    # Verify
    print(f"\nVerification: {'SUCCESS' if decrypted == test_message else 'FAILED'}")

    return cipher


if __name__ == "__main__":
    # Test with "writing proofs"
    # cipher_result = test_rsa()

    print("\n" + "=" * 50)

    # Now try user input cipher
    print("Test your cipher:")
    user_cipher = input("Enter your cypher (your encrypted message): ")
    decrypt_text(user_cipher)