f = open('input', 'r')
#o = open('output', 'w')
# Total amount of test cases
#t = int(f.readline())
t = 1

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

for x in range(1, t + 1):
    # Get stack without nl
    #l = f.readline().rstrip('\n')
    l = "6 3"
    n = int(l.split()[0])
    j = int(l.split()[1])
    c = 1
    o=[]
    
    while len(o) != j:
        cur = int('1' + (n - 2) * '0' + '1', 2)
        
        while not(True in [isprime(y) for y in [int(str(bin(cur))[2:], x) for x in range(2, 11)]]) and (str(bin(cur))[2] == '0' or str(cur)[-1] == '0'):
            cur = cur + 1
        
        o.append(cur - 1) 
        
    #o.write("Case #%s: %d\n" % (x, (c - 1)))



#o.close()
#f.close()