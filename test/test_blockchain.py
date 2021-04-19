import unittest
import hashlib
import json
from blockchain import Blockchain


class TestBlockchainMethods(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
        self.sender = "Santa Carlos"
        self.recipient = "Fernando"
        self.amount = 3

        self.proof = 100
        self.previous_hash = 1

    def test_genesis_block(self):
        genesis_block = self.blockchain.last_block["index"]
        self.assertEqual(genesis_block, 1)

    def test_new_transaction_return_type(self):
        transaction = self.blockchain.new_transaction(self.sender, self.recipient, self.amount)
        self.assertIsInstance(transaction, int)

    def test_new_block_return_type(self):
        block = self.blockchain.new_block(self.proof, self.previous_hash)
        self.assertIsInstance(block, dict)

    def test_hash_sha256(self):
        block = self.blockchain.new_block(self.proof, self.previous_hash)
        hash_ = self.blockchain.hash(block)

        self.assertIsInstance(hash_, str)
        self.assertEqual(hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest(), hash_)

    def test_proof_of_work(self):
        """

        """
        proof_assumption = self.blockchain.proof_of_work(self.proof)
        self.assertIsInstance(proof_assumption, int)
        self.assertEqual(proof_assumption, 35293)


if __name__ == '__main__':
    unittest.main()
