"""
KEY MANAGER

Generates temporary keys and encryption contexts.
Nothing is saved to disk.
"""

import phe.paillier as paillier
import tenseal as ts


class KeyManager:

    def __init__(self):

        print("\n--- Generating Encryption Keys ---")

        # PHE
        self.phePublicKey, self.phePrivateKey = (
            paillier.generate_paillier_keypair()
        )

        print("PHE keys generated.")

        # SHE - BFV
        self.sheContext = ts.context(
            ts.SCHEME_TYPE.BFV,
            poly_modulus_degree=4096,
            plain_modulus=1032193
        )

        print("SHE context generated.")

        # FHE - CKKS
        self.fheContext = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60]
        )

        self.fheContext.global_scale = 2 ** 40
        self.fheContext.generate_galois_keys()

        print("FHE context generated.")
        print("All temporary keys are ready.")