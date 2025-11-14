import hashlib
import json
from time import time #timestamp recording

class Blockchain:
    def __init__(self):
        self.current_transactions = [] 
        self.chain = []
        self.nodes = set()
        self.new_block(previous_hash=1, proof=100) #loop genesis block creation

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block
    #work for 11/09/25
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    #re-hashing (reminder :- make method for it later)
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """
        pass

    @property
    def last_block(self):
        """
        Returns the last Block in the chain
        """
        pass

#left to define proof_of_work, valid_proof, valid_chain, and conflict resolution method
#define api to p2p net bw nodes 
#implement proof validation method
#route mine methods to flask ka api calls
#create backend routes 