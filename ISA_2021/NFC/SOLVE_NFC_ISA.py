import socket
import libscrc


def connect_to_nfc():
    s = socket.socket()
    s.connect(('nfc.shieldchallenges.com',80))
    return s


def auth_pwd(): #MOVE TO AUTH STATE
    s = connect_to_nfc()
    pwd = bytearray()
    pwd.append(0x1B) #cmd
    pwd.append(0x24) #pwd
    pwd.append(0x68) #pwd
    pwd.append(0xBE) #pwd
    pwd.append(0xAF) #pd
    pwd.append(0x49) #CRC
    pwd.append(0x30) #CRC
    s.send(pwd)
    dataFromServer = s.recv(1024)
    if dataFromServer == b'\x01':
        print("ERROR")
        exit()
    else:
        print(f'PWD WORKED -> {dataFromServer} packet')
        better_page_reader(s)

def read_pages(soc):
    page = 0x4 #user memory starts at page 4
    for _ in range(9):
        BYTE_ARRAY = bytearray()
        BYTE_ARRAY.append(0x30) #cmd
        BYTE_ARRAY.append(page) #page
        CRC = hex(libscrc._crc16.iec14443_3_a(BYTE_ARRAY)) #GET CRC FOR COMMAND
        CRC_HIGH = int(CRC[2:4],16) 
        CRC_LOW = int(CRC[4:6],16)
        BYTE_ARRAY.append(CRC_LOW)  #input crc low to big (little endian)
        BYTE_ARRAY.append(CRC_HIGH)
        soc.send(BYTE_ARRAY)
        data_from_server = soc.recv(1024)
        print(data_from_server)
        page += 0x4 #READ COMMAND READS 4 PAGES AT A TIME 

def better_page_reader(soc):
    BYTE_ARRAY = bytearray()
    cmd = 0x3A #fast read
    start_page = 0x04
    end_page = 0x27
    BYTE_ARRAY.append(cmd)
    BYTE_ARRAY.append(start_page)
    BYTE_ARRAY.append(end_page)
    CRC = hex(libscrc._crc16.iec14443_3_a(BYTE_ARRAY))
    CRC_HIGH = int(CRC[2:4],16) 
    CRC_LOW = int(CRC[4:6],16)
    BYTE_ARRAY.append(CRC_LOW)
    BYTE_ARRAY.append(CRC_HIGH)
    soc.send(BYTE_ARRAY)
    data_from_server = soc.recv(1024)
    print(data_from_server)

def main():
    auth_pwd()


main()