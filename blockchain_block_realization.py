from datetime import datetime
import hashlib
from binascii import unhexlify, hexlify
import time

#Basic block realization
class Block:
    def __init__(self, prev_hash, transaction, amount):
        self.next = None
        #hidden for safety
        self.__data={
            "prev_hash": prev_hash,
            "transaction": transaction,
            "amount": amount,
            "hash": "",
            "time": datetime.now().time()
        }

        self.__data["hash"] = self.make_hash()

    #Get access to data, but without changing it
    def get_data(self):
        return self.__data

    #Make hash from previous hash parameter
    def make_hash(self):
        test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf-8")
        while test_hash[:5] != "00000": #More zeros means more complexity while computing
            test_hash = hexlify(hashlib.sha256(unhexlify(test_hash)).digest()).decode("utf-8")
        return test_hash


    def append(self, transaction, amount): #Append created hash
        n = self
        while n.next: #Go to the end of the chain
            n = n.next
        prev_hash = n.get_data()["hash"]
        end = Block(prev_hash, transaction, amount)
        n.next = end
    
#Function just to go through transactions
def printout_blocks(block):
    node = block
    print(node.get_data())
    while node.next:
        node = node.next
        print(node.get_data())


test_block = Block("00000d65048212c0fe54ef9eed65799e3c72ae793f337f89d553cc0992c02f79", "Ivan", 100) #Test operation from Ivan with amount = 100
test_block.append("Boris", 1423)
test_block.append("Mary", 99)

printout_blocks(test_block)
