from pwn import *



def foo(arg1,arg2):
    x = arg2+1 
    y = x ^ arg1
    z = y ^ 0x539    
    return z

def bar(arg1,arg2,arg3):
    x = arg3 +1
    z = x * arg2
    y = z + arg1
    return y


def result(func_str):
    func_str = func_str[2:-3] #slice
    func_str = (func_str.replace(' ','')) #remove spaces

   

    question_mark = (func_str.index('?'))

    if question_mark == (len(func_str)-1):
        x = func_str.split('=')
        func = x[0]
        return eval(func)
    else: #func_str[question_mark-1] == ',' or func_str[question_mark+1] == ',':
        func_str = func_str.replace('?','i')
        x = func_str.split('=')
        question = x[0]
        ans = x[1]
        for i in range(500000):
            test = eval(question)
            if test == int(ans):
                return i
   
def parse_input(serv):
    with open(r'C:\Users\aaron\Documents\GitHub\b01ler\res2.txt','w') as fi:
        for i in range (600):
            round = serv.recvline()
            msg = serv.recvline()
            func = serv.recvline()
            res = result(str(func))
            print(res)
            fi.writelines(f"{res}\n")
            serv.sendline((str(res)))
        
        

def decrypt():
    
    with open(r'C:\Users\aaron\Documents\GitHub\b01ler\res1.txt','r') as f:
        Loop_Counter = 49
        ls = [None]*500
        flag = ''
        for line in f:
            line = line.rstrip('\n')
            crypted_number = int(line)
            crypted_char = crypted_number & 0xff
            crypted_index = (crypted_number >> 8) & 0xff
            decrypted_index = crypted_index - Loop_Counter & 0xff
            ls[decrypted_index] = crypted_char
            
            Loop_Counter +=1
        key = 0
        for index,cryp in enumerate(ls):
            if cryp != None:
                flag += chr(cryp ^ ((17*(index-1)))&0xff)
        print(flag)



def main():
    conn = remote('shell.actf.co',21700)
    #--WELCOME--#
    print(conn.recvline())
    #parse_input(conn)
    decrypt()

main()