
"""
SHE DECRYPTION

Decrypts SHE encrypted data.
"""

import time
import os
import tenseal as ts


class SHEDecryption:

    def __init__(self, context):

        self.context = context

    def decrypt(self, ciphertext):

        result = ciphertext.decrypt()

        return result[0]

    def loadCiphertext(self, encryptedText):

        encryptedBytes = bytes.fromhex(
            encryptedText
        )

        ciphertext = ts.bfv_vector_from(
            self.context,
            encryptedBytes
        )

        return ciphertext

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

        print(f"\nSHE Decryption Time: {decryptionTime:.6f} seconds")

        return decryptedData
