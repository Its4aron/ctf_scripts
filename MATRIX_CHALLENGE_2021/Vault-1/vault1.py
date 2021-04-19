import random

# 1058463025 <-- brute forced code
# 110010011110001011000011110
# 1612994400 LOCAL 
# 1613001600 GMT
# 86400 <-- seconds in day

def search_seed():
    START_TIME = 1612994400 # epoch date
    size = 9
    FIND = '105846302'
    for seed in range(START_TIME,START_TIME+86400):
        random.seed(seed)
        x = ''.join(str((random.getrandbits(32)%10)) for x in range(size))
        if x.find(FIND) != -1:
            return seed

def get_pin(WORKING_SEED):
    random.seed(WORKING_SEED)
    pin = ''.join(str((random.getrandbits(32)%10)) for x in range(624))
    return pin

def main():
    pin = get_pin(search_seed())
    print(pin)

main()





# while 1:
#     for index,dig in enumerate(digits):
#         r.send(dig)
#         x = r.recv()
#         print(x)
#         if b'bye bye :)\n' in x:
#             r = remote('challenges.ctfd.io',30440)
#             r.recv()
#             r.send(b'\x31\n')
#             #START GUESSING
#             for c in correct_password:
#                 print(r.recv())
#                 r.send(c)
#             print(r.recv())
#         else:
#             correct_password.append(dig)
#             print(correct_password)
#             break
    



# START_TIME = 1612994400
# random.seed(START_TIME)
#     for i in range(START_TIME,START_TIME+86400):      
#         x = str(random.getrandbits(27))
#         if x.find('105846302') != -1:
#             print(x)

# size = 27
# START_TIME = 1612994400
# with open(r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\helper.txt','w') as f:  
#     for i in range(START_TIME,START_TIME+86400):
#         random.seed(i)   
#         for _ in range(624):       
#             x = ''.join(str(random.getrandbits(1)) for x in range(size))
#             x = random.getrandbits(27)
#             x = str(int(x,2))
#             x = str(x)
#             x += '\n'
#             f.write(x)
#             if x.find('105846302') != -1:
#                 print('-'*80)























# import random
# import string
# size = 1
# START_TIME = 1612994400
# for i in range(START_TIME,START_TIME+86400):
#     random.seed(i)
#     x = ''.join(str(random.getrandbits(32)) for x in range(size))
#     if x.find('105846302') != -1:
#         print(x)

#--------------------------------------------------------------------------------------

# looking_for = 1058463025
# binary = ''

# with open(r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\helper.txt','w') as f:
#     for i in range(START_TIME,START_TIME+86400):
#         random.seed(i)
        
#         x += '\n'
#         f.write(x)



#--------------------------------------------------------------------------------------
# looking_for = '105846302'
# import random, time
# from randcrack import RandCrack
# START_TIME = 1612994400

# with open(r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\helper.txt','w') as f:
#     for i in range(START_TIME,START_TIME+86400):
#         random.seed(i)
#         rc = RandCrack()
#         for i in range(624):
#             rc.submit(random.getrandbits(32))
#         x = str(rc.predict_getrandbits(64))
#         f.write(x)
#         if x.find(looking_for) != -1:
#             print(i)