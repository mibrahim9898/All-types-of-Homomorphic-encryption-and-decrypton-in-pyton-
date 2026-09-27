
"""
SOMEWHAT HOMOMORPHIC ENCRYPTION

SHE encryption using TenSEAL BFV.
"""

from originalData.filesize import FileSize
import time
import tenseal as ts
import os


class SHE:

    fileSize = FileSize()

    def __init__(self, context):

        self.context = context

    def encrypt(self, message):

        encryptedMessage = ts.bfv_vector(
            self.context,
            [int(message)]
        )

        return encryptedMessage

    def addEncrypted(self, cipher1, cipher2):

        result = cipher1 + cipher2

        return result

    def multiplyEncrypted(self, cipher1, cipher2):

        result = cipher1 * cipher2

        return result

    def encryptFile(self, inputFile, outputFile):

        data = []

        try:

            with open(inputFile, "r") as file:

                for line in file:

                    line = line.strip()

                    if line:

                        number = int(line)

                        data.append(number)

            print(f"Read {len(data)} numbers: {data}")

        except FileNotFoundError:

            data = [2, 3, 4, 5]

            print(f"{inputFile} not found.")
            print(f"Using test data: {data}")

        # Original file size
        if os.path.exists(inputFile):

            originalSize = self.fileSize.getFileSize(
                inputFile
            )

            print(
                f"Original File Size: "
                f"{originalSize} bytes"
            )

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
            f"\nSHE Encryption Time: "
            f"{encryptionTime:.6f} seconds"
        )

        os.makedirs(
            os.path.dirname(outputFile),
            exist_ok=True
        )

        with open(outputFile, "w") as file:

            for cipher in encryptedData:

                file.write(
                    cipher.serialize().hex() + "\n"
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
