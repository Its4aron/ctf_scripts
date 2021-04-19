import string


to_sort = []*144 #global list of all possible answers for each offset

def f2(esi,off):
    ans=[off] #start answer list with offset
    for c in string.printable:
        c = ord(c)
        new_c = c & 0xf
        if new_c == esi:
            ans.append(chr(c))
    to_sort.append(ans)
    return ans
    
def f1(esi,off):
    ans=[off] #start answer list with offset
    for c in string.printable:
        c = ord(c)
        new_c = c >> 4
        if new_c == esi:
            ans.append(chr(c))
    to_sort.append(ans)
    return ans


def f3(esi,off):
    ans=[off] #start answer list with offset
    esi = ~esi
    esi = esi & 0xf
    for c in string.printable:
        c = ord(c)
        new_c = c >> 4
        if new_c == esi:
            ans.append(chr(c))

    to_sort.append(ans)
    return ans

def f4(esi,off):
    ans=[off] #start answer list with offset
    esi = ~esi
    esi = esi & 0xf
    for c in string.printable:
        c = ord(c)
        new_c = c & 0xf
        if new_c == esi:
            ans.append(chr(c))
    to_sort.append(ans)
    return ans


def create_code(PATH): 
    ls = ['A']*144 #list "Stack"
    c = 0
    with open(PATH, 'r') as f:
        for line in f:
            if line.find('rbp') != -1: #Collect offset in the stack
                offset = line[(line.find('rbp')+4):-2]
                c+=1
            elif line.find('esi') != -1: #Collect the esi
                esi = line[(line.find('esi')+4):-1]
                c+=1
            elif line.find('call') != -1: # Collect function
                func = line[(line.find('call')+23):-2]
                c+=1
            if c == 3: #COLLECTED RBP,ESI,CALL
                c = 0
                offset_dec = (int(offset,16)) #convert to decimal
                esi = (int(esi,16))
                x = eval(func + f"({esi},{offset})") #return value
                ls[-offset_dec] = x #add to list (stack)
        flag = ''
        for i in range(0,len(sorted(to_sort)),2): # go over and skip
            chitoch = (set(sorted(to_sort)[i])&set(sorted(to_sort)[i+1])) # collect the simillar dots
            for dot in chitoch:
               if type(dot) == str:
                   flag += dot
        flag = flag[::-1]
        print(flag)
        

  
               
        
def main():
    path = r'C:\Users\aaron\Documents\GitHub\Matrix_CTF\asm_code_matrix_Ctf.txt'
    create_code(path)
  

main()










