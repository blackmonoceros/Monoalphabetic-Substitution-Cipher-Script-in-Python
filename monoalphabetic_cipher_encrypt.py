import string

def monoalphabetic_cipher_encrypt(plaintext, key):
    """
    Encrypts the given plaintext using a monoalphabetic substitution cipher.
    
    :param plaintext: The text to be encrypted
    :param key: A permutation of the alphabet (26 unique letters for the English alphabet)
    :return: The encrypted text
    """
    alphabet = string.ascii_lowercase  # Standard alphabet: 'abcdefghijklmnopqrstuvwxyz'
    cipher_map = {alphabet[i]: key[i] for i in range(len(alphabet))}  # Create substitution mapping
    encrypted_text = ""
    
    for char in plaintext.lower():  # Convert to lowercase for consistency
        if char in cipher_map:
            encrypted_text += cipher_map[char]
        else:
            encrypted_text += char  # Leave non-alphabetic characters unchanged
    
    return encrypted_text

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    key = "qwertyuiopasdfghjklzxcvbnm"  # Example key (a permutation of the alphabet)
    
    if len(key) != 26 or not set(key).issubset(set(string.ascii_lowercase)):
        print("Error: The key must be a permutation of the alphabet (26 unique letters).")
    else:
        encrypted = monoalphabetic_cipher_encrypt(plaintext, key)
        print(f"Encrypted text: {encrypted}")