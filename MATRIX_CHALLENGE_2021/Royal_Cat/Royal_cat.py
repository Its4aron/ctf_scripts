from struct import *

def collect_FromStack():
    with open(r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\stackdump.dat', 'rb') as f:
        stackbuf = f.read()
        stackbuf_words = unpack('i'*(len(stackbuf)//4), stackbuf) #sets of double words
    return stackbuf_words

def decrypt_stack(stackbuf_words): #reversed validate
    result = []
    for ofs in range(len(stackbuf_words)): #Go over all the offsets in the stack_buffer
        if stackbuf_words[ofs]: #CHECK'S FOR 0
            if ofs & 1: 
                result.append(((stackbuf_words[ofs] ^ 0x52) // 2) - 0x62) #Odd number
            else:
                result.append(((stackbuf_words[ofs] ^ 0x64) // 4) - 0x45) #Even number
    return result


def create_RoyalCat(result):
    with open(r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\RoyalCat', 'wb') as f:
        f.write(bytes(result)) #write the correct file 


def main():
    print(collect_FromStack())
    # create_RoyalCat(decrypt_stack(collect_FromStack()))

main()
