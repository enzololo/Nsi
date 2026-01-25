from timeit import default_timer as time

def recherche(l, x, d, f):
    if d == f:
        return l[d] == x
    m = (d + f) // 2
    return recherche(l, x, d, m) or recherche(l, x, m + 1, f)

def recherchedi(l, x, d, f):
    if d > f:
        return False
    m = (d + f) // 2
    if l[m] == x:
        return True
    elif l[m] > x:
        return recherchedi(l, x, d, m - 1)
    else:
        return recherchedi(l, x, m + 1, f)
    
    
l = [95, 28, 36, 52, 85, 56, 34, 59, 17, 26, 16, 25, 69, 98, 4, 85, 81, 48, 11, 57]
start = time()
recherche(l, 57, 0, len(l)-1)
end = time()
print(end-start)

L =	[4, 11, 16, 17, 25, 26, 28, 34, 36, 48, 52, 56, 57, 59, 69, 81, 85, 85, 95, 98]
start = time()
recherche(L, 57, 0, len(l)-1)
end = time()
print(end-start)

def simple(l,x):
    for elt in l:
        if x == elt:
            return True
        
start = time()
simple(l,57)
end = time()
print(end-start)
    
        
