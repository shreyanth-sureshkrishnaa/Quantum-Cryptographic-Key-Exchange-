# This file is not technically a part of the main Quantum Encryption framework.
# This file covers the AES encryption process so that a firm foundation can be built underneath the more complex structures which await. 

# ------- # 

# cryptography is a widely used vetted library. Hazmat contains lower level primitives.
# AESGCM is an AEAD (Authenticated Encryption with Associated Data) implementation that provides AES in Galois/Counter Mode (GCM), including authentication tags.
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# We're importing OS here so that we can use os.random() to generate cryptographically secure randomized bytes.
import os


# The main function here, EncryptMessage takes a symmetric key and a plaintext string and returns a tuple containing the nonce and the ciphertext.
# 'nonce' stands for 'number used once'. It is NOT secret.
# A nonce basically makes sure that ciphertext never looks the same twice. 
def EncryptMessage(aesKey: bytes, plainText: str) -> tuple:

    aesGcm = AESGCM(aesKey) 
    nonce = os.urandom(12)  # 96-bit nonce (recommended size for GCM)
    cipherText = aesGcm.encrypt(nonce, plainText.encode(), None)
    return nonce, cipherText

# This function takes the AES key, the nonce, and the ciphertext+tag and returns the original plaintext string.
# However, I will not be using it here. There exists a separate decrypter.
def DecryptMessage(aesKey: bytes, nonce: bytes, cipherText: bytes) -> str:

    aesGcm = AESGCM(aesKey)
    plainText = aesGcm.decrypt(nonce, cipherText, None)
    return plainText.decode()

if __name__ == "__main__":

    # Note: Keys, nonces, and ciphertexts are almost always displayed or stored in hex (or Base64) in real-world cryptographic tools.
    # Hex is human-friendly. Also, bytes often contain non-printable characters.

    aesKey = AESGCM.generate_key(bit_length=256)
    print(f"AES Key: {aesKey.hex()}")

    originalMessage = input("Enter in your message: ")
    print(f"Original message: {originalMessage}")

    nonce, cipherText = EncryptMessage(aesKey, originalMessage)
    print(f"Nonce: {nonce.hex()}")
    print(f"Ciphertext: {cipherText.hex()}")