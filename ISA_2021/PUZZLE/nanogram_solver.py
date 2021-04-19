from itertools import product
'''
OUT SORUCED FROM REDDIT
'''
def seed_possible(size,pieces):
    """
    All possible postions
    """    
    max_ = size - sum(pieces) - len(pieces) + 2
    a = list(range(max_))
    b = list(range(1,max_+1))
    L = [a]
    for p in pieces[:-1]:
        L.append([p])
        L.append(b)
    L.append([pieces[-1]])
    L.append(a)
        
    def yes_no(a_list):
        for x,y in zip(a_list[::2],a_list[1::2]):
            for _ in range(x):
                yield 0
            for _ in range(y):    
                yield 1
        for _ in range(a_list[-1]):    
            yield 0
    P = []
    for x in product(*L):
        if sum(x) == size:
            P.append(list(yes_no(x)))  
    return P
  
def process(num_columns, num_rows, columns, rows):
    """
    Format input
    """
    def proc_seed(num_x, inx):
        num_x = int(num_x)
        x = [[int(y) for y in x.split(',')] for x in inx.strip('"').split('","')]
        return [seed_possible(num_x,v) for v in x]
    
    Colums = proc_seed(num_columns, columns)
    Rows = proc_seed(num_rows, rows)
    return Colums, Rows
        
def intersect(a_list, b_list, ix_a, ix_b):
    """
    Takes two list and intersects them at a specific coordinate
    """
    a_list = [list(x) for x in set(tuple(y) for y in a_list)]
    a_set = set(x[ix_b] for x in a_list)
    b_set = set(x[ix_a] for x in b_list)
    ix_v = a_set & b_set
    
    def is_in(x): 
        a_list,ix = x
        return [x for x in a_list if x[ix] in ix_v]
    
    new_a, new_b = map(is_in,((a_list, ix_b), (b_list, ix_a)))
    return new_a, new_b, (a_list != new_a or b_list != new_b )

def solve(horizon, vertica):
    """
    Intersects all possibilities brute force untill a solution is found
    """
    limx = len(horizon)
    #while sum(len(x) for x in horizon) > limx:
    changed = True
    while changed:
        changed =  False
        for ix, a_list in enumerate(horizon):
            for iy, b_list in enumerate(vertica):
                new_a, new_b, change = intersect(a_list,b_list,ix,iy)
                if change:
                    changed = True
                    horizon[ix] = new_a
                    vertica[iy] = new_b
        for ix, a_list in enumerate(vertica):
            for iy, b_list in enumerate(horizon):
                new_a, new_b, change = intersect(a_list,b_list,ix,iy)
                if change:
                    changed = True
                    vertica[ix] = new_a
                    horizon[iy] = new_b      
    return vertica
    
def show(problem):
    ps = problem.split('\n')
    a,b = process(*ps)
    vertica = solve(a,b)
    print(vertica)
    D = {0:'.',1:'*'}
    print('\n'.join(''.join(D[c] for c in col[0]) for col in vertica))



show('''25
25
"7","12","3,2,2,4","4,2,2,2","2,2,2,2,2","3,2,2,2,2","4,2,2,2,2","4,2,2,2,2","1,2,2,2,2,2","2,2,2,2,2,2","2,2,2,2,2,2","4,2,2,2,2","3,2,2,2,2","2,2,2,2,2","2,4,2,2,2","5,2,2,2","3,2,2,2","2,3,2,2","7,2,2","4,3,2","2,3,2","2,4,3","4,3","13","9"
"8","13","3,2,5","8,2,3","8,2,4","2,2,2,2","13,2,2","12,2,3","1,2,4","17,2,2","16,3,2","2,2,2","2,3,2","19,2","17,2","2,2","2,2","2,2","2,2","2,2","2,2","2,3","3,3","13","9"''')