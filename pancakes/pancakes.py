f = open('B-large.in', 'r')
o = open('output', 'w')
# Total amount of test cases
t = int(f.readline())

for x in range(1, t + 1):
    # Get stack without nl
    l = f.readline().rstrip('\n')
    n = l.split()[0]
    j = l.split()[1]
    c = 1
    o=[]
    
    while len(o) != j:
        cur = 0
        
        while True in [isprime(y) for y in [int(str(bin(cur))[2:], x) for x in range(2, 11)]] and (str(bin(cur))[2] == 1 and str(cur)[-1] == 1):
                cur = cur + 1
        
        o.append(cur - 1) 
        
    o.write("Case #%s: %d\n" % (x, (c - 1)))

def isprime(n):
    n = abs(int(n))
    
    if n == 2: 
        return True    

    if not n & 1 or n < 2: 
        return False
        
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

o.close()
f.close()