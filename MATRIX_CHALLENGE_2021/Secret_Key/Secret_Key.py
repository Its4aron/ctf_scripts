# lights = 985246f1480134f60eeeb9e8c2d08910 #32

# {OÙ§lP’Úó­Ôd'iý»?a˜è<ÖúQé~ù
 #32

# ciphertext = "{OÙ§lP’Úó­Ôd'iý»?a˜è<ÖúQé~ù"
# key = b'985246f1480134f60eeeb9e8c2d08910'
# cipher = AES.new(key, AES.MODE_CBC)
# plaintext = cipher.decrypt(ciphertext)
# print(plaintext)

# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# iv = '985246f1480134f60eeeb9e8c2d08910'
# iv = binascii.unhexlify(iv)
# key = b'f1b83682fa9cbe59cacba59d0ae9af44'
# #FILE--
# input_file = 'enc.txt'
# file_in = open(input_file, 'rb')
# ciphered_data = file_in.read()
# file_in.close()
# #FILE--
# #Cipher--
# cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher

# original_data = (cipher.decrypt(ciphered_data), AES.block_size)
# print(original_data)

# x = b'\xbb\x03({\xabl\xf4\xf1}\xf9\xd1\x96dQ[{Xx%\xf2\x01\x15\xa5\xb0qi\xf1\xe6Y\xc5\x0e\x84'
# x = binascii.b2a_hex(x)
# print(x)
import binascii
from Crypto.Cipher import AES

def decrypt(key,IV):
    IV = binascii.unhexlify(IV)
    key = bytes.fromhex(key)
    aes = AES.new(key, AES.MODE_CBC, IV)
    with open(r"C:\Users\aaron\Documents\GitHub\Matrix_CTF\enc.txt", "rb") as f:
        d = f.read()
    d = aes.decrypt(d)
    return d

def main():
    IV="985246f1480134f60eeeb9e8c2d08910"
    KEY = "f1b83682fa9cbe59cacba59d0ae9af44"
    print(decrypt(KEY,IV))

main()


#########python 2
'''
from secretsharing import SecretSharer
shares = [
    "1-9362e50f3be0a411a75b55086b9b34f796dbeef58c498edcc185e3a3dc0bf905",
    "2-c58c3821a12d58e854922d0b3856ebf01692bbca7b9637cebb4e2cc6934859c",
    "3-6ae19b589a96947699c96958d7bead57315fecd84cec3c3a4958a316b263575b",
    "4-aefd6c92bd6be0c9e4dc28a0d846f0c026c032487be21914da712482b7986d19",
    "5-d8ac37308292ba88668160a8b51e38f9e189fc0d349afa0c9efe671078d3c6d6",
]
a = SecretSharer.recover_secret(shares[0:3]) #take first 3 entites 
print(a)
'''
######### output: f1b83682fa9cbe59cacba59d0ae9af44


'''
1111 1111
1111 1111
1111 1111
1001 1000 
0101 0010
0100 0110
1111 0001
0100 1000
0000 0001
0011 0100
1111 0110
0000 1110
1110 1110
1011 1001
1110 1000
1100 0010
1101 0000
1000 1001
0001 0000
1111 1111
1111 1111
1111 1111
'''