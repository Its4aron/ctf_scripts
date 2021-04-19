import libscrc



def gen_all_hex(): #collect all combinations for PIN
    i = 0
    while i < 16**4:
        yield "{:04X}".format(i)
        i += 1


def brute_force():
    brute_this = '0x3049' #CRC TO FIND
    for hexy in gen_all_hex():
        fix_it = f'1B{str(hexy)}BEAF' #shabak msg
        brand_new_hexy = hex(int(fix_it, base = 16)) 
        byte_array = bytes.fromhex(brand_new_hexy[2::]) 
        x = hex(libscrc._crc16.iec14443_3_a(byte_array)) #CRC MSG 
       
        if x == brute_this: #CHECK MATCH 
            print(f"found a match with --> {hexy}")
            break



brute_force()


