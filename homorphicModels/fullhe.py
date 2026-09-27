"""
FULL HOMOMORPHIC ENCRYPTION

FHE encryption using TenSEAL CKKS.
"""

import time
import tenseal as ts
import os


class FHE:

    def __init__(self, context):

        self.context = context

    def encrypt(self, message):

        encryptedMessage = ts.ckks_vector(
            self.context,
            [message]
        )

        return encryptedMessage

    def addEncrypted(self, cipher1, cipher2):

        result = cipher1 + cipher2

        return result

    def multiplyEncrypted(self, cipher1, cipher2):

        result = cipher1 * cipher2

        return result

    def decrypt(self, ciphertext):

        result = ciphertext.decrypt()

        return result[0]

    def encryptFile(self, inputFile, outputFile):

        data = []

        try:

            with open(inputFile, "r") as file:

                for line in file:

                    line = line.strip()

                    if line:

                        number = float(line)

                        data.append(number)

            print(f"Read {len(data)} numbers: {data}")

        except FileNotFoundError:

            data = [2.0, 3.0, 4.0, 5.0]

            print(f"{inputFile} not found.")
            print(f"Using test data: {data}")

        encryptedData = []

        # Start encryption timer
        start_time = time.perf_counter()

        for number in data:

            cipher = self.encrypt(number)

            encryptedData.append(cipher)

            print(f"E({number}) created.")

        # Stop encryption timer
        end_time = time.perf_counter()

        encryptionTime = end_time - start_time

        print(f"\nFHE Encryption Time: {encryptionTime:.6f} seconds")

        outputDirectory = os.path.dirname(outputFile)

        if outputDirectory:
            os.makedirs(outputDirectory, exist_ok=True)

        with open(outputFile, "w") as file:

            for cipher in encryptedData:

                file.write(
                    cipher.serialize().hex() + "\n"
                )

            cipherSize = os.path.getsize(outputFile)

        print(
            f"Ciphertext File Size: "
            f"{cipherSize} bytes"
        )
        print(f"Encrypted data saved to {outputFile}")

        return encryptedData, data
