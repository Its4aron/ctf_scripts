import requests
import json
import base64
import jwt


def start_key(ID):

    payload = {"username":"Test_User","password":"SecretPassw0rd","puzzle_id":ID}
    r = requests.get('http://puzzle.shieldchallenges.com/api/token',json=payload)
    pay = json.loads(r.text)
    token = pay["token"]
    return token


def write_at_dot(x,y,ls): #OLD WRITING FUNCTION
    ls.append('000003')
    for i in range(x):
        ls.append('000001')
    for i in range(y):
        ls.append('000005')
    ls.append('000007')
    

def solve_puzzle(starting_token,ID,PATH):
    instructions_list = [] #list to draw the list
    instructions_list.append('000003') # set cursor to zero on the map
    with open(PATH, 'r') as f:
        for line in f:
            for c in line:
                if c == '\n':
                    continue
                if c == '*':
                    instructions_list.append('000007')#draw X on current cursor 
                instructions_list.append('000001') #shift right

            instructions_list.append('000005') #go down
    
    #print(instructions_list)
    token = starting_token
    for inst in instructions_list:
        payload = {"instructions":inst}
        res = requests.patch(f'http://puzzle.shieldchallenges.com/api/puzzle/{ID}',headers={'Authorization':f'Bearer {token}'},json=payload)
        ans = json.loads(res.text)
        #print(f'do not look unless its something cool :{ans}')
        try:
            token = ans["token"] #update token
        except:
            #print(f"FLAG: {ans}")
            return ans
            break
        decoded_token = token.split('.')[1] + '==='
        decoded_token = base64.b64decode(decoded_token)
        print(f"{decoded_token} instruction = {inst}")
    return token

def main():
    ID = '3'
    PATH = r'C:\Users\aaron\Documents\GitHub\CTF_Work\TopSecret_answer.txt'
    start_token = start_key(ID)
    flag_answer = solve_puzzle(start_token,ID,PATH)
    flag = flag_answer["flag"]
    print(f'FOUND THE FLAG: -------------- {flag} ------------- :FOUND THE FLAG')
    
    

main()