"""
PHE DECRYPTION

Decrypts PHE encrypted data.
"""

import os
import time
from phe.paillier import EncryptedNumber


class PHEDecryption:

    def __init__(self, publicKey, privateKey):

        self.publicKey = publicKey
        self.privateKey = privateKey

    def decrypt(self, encryptedMessage):

        decryptedMessage = self.privateKey.decrypt(
            encryptedMessage
        )

        return decryptedMessage

    def loadCiphertext(self, encryptedText):

        encryptedNumber = EncryptedNumber(
            self.publicKey,
            int(encryptedText)
        )

        return encryptedNumber

    def decryptFile(self, inputFile):

        decryptedData = []

        # Start decryption timer
        start_time = time.perf_counter()

        with open(inputFile, "r") as file:

            for line in file:

                line = line.strip()

                if line:

                    cipher = self.loadCiphertext(line)

                    message = self.decrypt(cipher)

                    decryptedData.append(message)

        # Ciphertext file size
        cipherSize = os.path.getsize(inputFile)

        print(
            f"\nCiphertext File Size: "
            f"{cipherSize} bytes"
        )

        # Stop decryption timer
        end_time = time.perf_counter()

        decryptionTime = end_time - start_time

        print(f"\nPHE Decryption Time: {decryptionTime:.6f} seconds")

        return decryptedData
