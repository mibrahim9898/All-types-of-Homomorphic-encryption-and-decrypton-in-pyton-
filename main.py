"""
HOMOMORPHIC ENCRYPTION

Main program for PHE, SHE and FHE.

Temporary keys are generated once
when the program starts.
"""

from keygenrator.key import KeyManager

from homorphicModels.partialhe import PHE
from homorphicModels.somewhat import SHE
from homorphicModels.fullhe import FHE

from decryptedData.partialhedecrytpion import PHEDecryption
from decryptedData.somewhatdec import SHEDecryption
from decryptedData.fullhedecryption import FHEDecryption


def main():

    # Generate all temporary keys once
    keyManager = KeyManager()

    # PHE objects
    phe = PHE(
        keyManager.phePublicKey
    )

    pheDecryption = PHEDecryption(
        keyManager.phePublicKey,
        keyManager.phePrivateKey
    )

    # SHE objects
    she = SHE(
        keyManager.sheContext
    )

    sheDecryption = SHEDecryption(
        keyManager.sheContext
    )

    # FHE objects
    fhe = FHE(
        keyManager.fheContext
    )

    fheDecryption = FHEDecryption(
        keyManager.fheContext
    )

    while True:

        print("HOMOMORPHIC ENCRYPTION")

        print("PHE")
        print("1. PHE Encryption")
        print("2. PHE Decryption")

        print("SHE")
        print("3. SHE Encryption")
        print("4. SHE Decryption")

        print("FHE")
        print("5. FHE Encryption")
        print("6. FHE Decryption")

        print("Other")
        print("7. Run All Three")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        # =====================================================
        # PHE ENCRYPTION
        # =====================================================

        if choice == "1":

            print("\n" + "=" * 60)
            print("PHE ENCRYPTION")
            print("=" * 60)

            phe.encryptFile(
                "original_files/dataP.txt",
                "encrypted_files/phe_encrypted.txt"
            )

        # =====================================================
        # PHE DECRYPTION
        # =====================================================

        elif choice == "2":

            print("\n" + "=" * 60)
            print("PHE DECRYPTION")
            print("=" * 60)

            try:

                decryptedData = pheDecryption.decryptFile(
                    "encrypted_files/phe_encrypted.txt"
                )

                print(
                    f"\nDecrypted PHE Data: "
                    f"{decryptedData}"
                )

            except FileNotFoundError:

                print(
                    "\nPHE encrypted file not found."
                )

        # =====================================================
        # SHE ENCRYPTION
        # =====================================================

        elif choice == "3":

            print("\n" + "=" * 60)
            print("SHE ENCRYPTION")
            print("=" * 60)

            she.encryptFile(
                "original_files/dataS.txt",
                "encrypted_files/she_encrypted.txt"
            )

        # =====================================================
        # SHE DECRYPTION
        # =====================================================

        elif choice == "4":

            print("\n" + "=" * 60)
            print("SHE DECRYPTION")
            print("=" * 60)

            try:

                decryptedData = sheDecryption.decryptFile(
                    "encrypted_files/she_encrypted.txt"
                )

                print(
                    f"\nDecrypted SHE Data: "
                    f"{decryptedData}"
                )

            except FileNotFoundError:

                print(
                    "\nSHE encrypted file not found."
                )

        # =====================================================
        # FHE ENCRYPTION
        # =====================================================

        elif choice == "5":

            print("\n" + "=" * 60)
            print("FHE ENCRYPTION")
            print("=" * 60)

            fhe.encryptFile(
                "original_files/dataF.txt",
                "encrypted_files/fhe_encrypted.txt"
            )

        # =====================================================
        # FHE DECRYPTION
        # =====================================================

        elif choice == "6":

            print("\n" + "=" * 60)
            print("FHE DECRYPTION")
            print("=" * 60)

            try:

                decryptedData = fheDecryption.decryptFile(
                    "encrypted_files/fhe_encrypted.txt"
                )

                print(
                    f"\nDecrypted FHE Data: "
                    f"{decryptedData}"
                )

            except FileNotFoundError:

                print(
                    "\nFHE encrypted file not found."
                )

        # =====================================================
        # RUN ALL THREE
        # =====================================================

        elif choice == "7":

            print("\n" + "=" * 60)
            print("RUNNING ALL THREE ENCRYPTION TYPES")
            print("=" * 60)

            # ---------------- PHE ----------------

            print("\n========== PHE ==========")

            encryptedPHE, originalPHE = phe.encryptFile(
                "original_files/dataP.txt",
                "encrypted_files/phe_encrypted.txt"
            )

            if len(encryptedPHE) >= 2:

                encryptedResult = (
                    encryptedPHE[0] + encryptedPHE[1]
                )

                decryptedResult = (
                    pheDecryption.decrypt(
                        encryptedResult
                    )
                )

                expectedResult = (
                    originalPHE[0] + originalPHE[1]
                )

                print(
                    f"\nPHE Addition Result: "
                    f"{decryptedResult}"
                )

                print(
                    f"Expected Result: "
                    f"{expectedResult}"
                )

            # ---------------- SHE ----------------

            print("\n========== SHE ==========")

            encryptedSHE, originalSHE = she.encryptFile(
                "original_files/dataS.txt",
                "encrypted_files/she_encrypted.txt"
            )

            if len(encryptedSHE) >= 2:

                encryptedResult = (
                    encryptedSHE[0] * encryptedSHE[1]
                )

                decryptedResult = (
                    sheDecryption.decrypt(
                        encryptedResult
                    )
                )

                expectedResult = (
                    originalSHE[0] * originalSHE[1]
                )

                print(
                    f"\nSHE Multiplication Result: "
                    f"{decryptedResult}"
                )

                print(
                    f"Expected Result: "
                    f"{expectedResult}"
                )

            # ---------------- FHE ----------------

            print("\n========== FHE ==========")

            encryptedFHE, originalFHE = fhe.encryptFile(
                "original_files/dataF.txt",
                "encrypted_files/fhe_encrypted.txt"
            )

            if len(encryptedFHE) >= 3:

                encryptedAdd = fhe.addEncrypted(
                    encryptedFHE[0],
                    encryptedFHE[1]
                )

                encryptedResult = (
                    fhe.multiplyEncrypted(
                        encryptedAdd,
                        encryptedFHE[2]
                    )
                )

                decryptedResult = (
                    fheDecryption.decrypt(
                        encryptedResult
                    )
                )

                expectedResult = (
                    (originalFHE[0] + originalFHE[1])
                    * originalFHE[2]
                )

                print(
                    f"\nFHE Result: "
                    f"{decryptedResult}"
                )

                print(
                    f"Expected Result: "
                    f"{expectedResult}"
                )

            print("\n" + "=" * 60)
            print("ALL THREE COMPLETED")
            print("=" * 60)

        # =====================================================
        # EXIT
        # =====================================================

        elif choice == "8":

            print("\nProgram ended.")

            break

        else:

            print("\nInvalid choice.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":

    main()