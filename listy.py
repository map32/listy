def validpass(p):
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = "abcdefghijklmnopqrstuvwxyz"
    n = "0123456789"
    return len([a for a in p if a in u]) * len([b for b in p if b in l]) * len([c for c in p if c in n]) != 0

def evalpass(p):
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = "abcdefghijklmnopqrstuvwxyz"
    n = "0123456789"
    a = len([a for a in p if a in u])
    b = len([a for a in p if a in l])
    c = len([a for a in p if a in n])
    d = len(p)-a-b-c
    score(a,len(p))
    score(b,len(p))

def score(x,n):
    return -x(x-n/2.)
