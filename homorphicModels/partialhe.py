"""
PARTIALLY HOMOMORPHIC ENCRYPTION

PHE encryption using Paillier.
"""

from originalData.filesize import FileSize
import time
import os


class PHE:

    fileSize = FileSize()

    def __init__(self, publicKey):

        self.publicKey = publicKey

    def encrypt(self, message):

        encryptedMessage = self.publicKey.encrypt(message)

        return encryptedMessage

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

            data = [10, 20, 30, 40]

            print(f"{inputFile} not found.")
            print(f"Using test data: {data}")

        # Original file size
        if os.path.exists(inputFile):

            originalSize = self.fileSize.getFileSize(inputFile)

            print(f"Original File Size: {originalSize} bytes")

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

        print(
            f"\nPHE Encryption Time: "
            f"{encryptionTime:.6f} seconds"
        )

        os.makedirs(
            os.path.dirname(outputFile),
            exist_ok=True
        )

        with open(outputFile, "w") as file:

            for cipher in encryptedData:

                file.write(
                    str(cipher.ciphertext()) + "\n"
                )

        print(f"Encrypted data saved to {outputFile}")


        # Encrypted file size
        encryptedSize = self.fileSize.getFileSize(
            outputFile
        )

        print(
            f"Encrypted File Size: "
            f"{encryptedSize} bytes"
        )

        return encryptedData, data
