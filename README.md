# Monoalphabetic-Substitution-Cipher-Script-in-Python

Description of the Monoalphabetic Substitution Cipher.

The monoalphabetic substitution cipher is a simple encryption method where each letter in the plaintext is replaced with another letter according to a fixed substitution key. 
The key is a permutation of the alphabet, meaning each letter in the alphabet is mapped to a unique letter. For example, if the key maps "A" to "D", "B" to "E", and so on, the 
plaintext "ABC" would be encrypted as "DEF".
Python Script
The user provides the plaintext and the substitution key (a permutation of the alphabet).

How the Script Works ?

Alphabet and Key:
The script uses the English alphabet (abcdefghijklmnopqrstuvwxyz).
The key is a permutation of the alphabet, such as "qwertyuiopasdfghjklzxcvbnm". Each letter in the plaintext is substituted with the corresponding letter in the key.
Encryption Process:
A dictionary (cipher_map) is created to map each letter of the alphabet to its corresponding letter in the key.
The plaintext is processed character by character. If a character is in the alphabet, it is replaced using the cipher_map. Non-alphabetic characters (e.g., spaces, punctuation) 
are left unchanged.
Example Execution:
Plaintext: "hello world"
Key: "qwertyuiopasdfghjklzxcvbnm"
Encrypted Text: "itssg vgksr"
Key Points
Key Validation: The script ensures that the key is a valid permutation of the alphabet (26 unique letters).
Case Sensitivity: The script converts all input to lowercase for simplicity. It can be extended to handle uppercase letters if needed.
Non-Alphabetic Characters: Characters like spaces, numbers, and punctuation are not encrypted and remain unchanged.
Security Note
While the monoalphabetic substitution cipher is simple and easy to implement, it is not secure by modern standards. It can be easily broken using frequency analysis, as the 
frequency of letters in the ciphertext will match the frequency of letters in the plaintext language.
