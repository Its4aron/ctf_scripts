



def decompress(pairs):
    dec = "" #Decompressed string
    next_code = 1 #Code for substrings
    code_decrypt = {} #dictionry 
    for pair in pairs:
        first_half = pair[0]
        second_half = pair[1]
        if first_half == 0: 
            dec += second_half
            code_decrypt[next_code] = second_half
            next_code +=1
        else:
            actual_string = code_decrypt[first_half] + second_half
            dec += actual_string
            code_decrypt[next_code] = actual_string
            next_code +=1

    return dec

def main():
    ENC_BYTES_STR = "0062 0063 0074 0066 007B 0077 006F 0072 0064 076E 0073 066F 0864 0B6F 006E 0A77 0772 0973 0C72 1277 1164 0B7D"
    splited = ENC_BYTES_STR.split(" ")
    pairs = [(int(element[:2],16), chr(int(element[2:],16))) for element in splited] #split on index and on char
    print(decompress(pairs))



if __name__ == "__main__":
    main()