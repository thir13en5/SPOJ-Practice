t = int(input())

def sieve(l,u):
    non_primes = [0,1]
    primes = []
    for num in range(u+1):
        if num not in non_primes:
            i = 1
            while(num*i <= u):
                non_primes.append(num*i)
                i+=1
            primes.append(num)
    return primes
for t_i in range(t):
    lower, upper = map(int, input().split())
    primes = sieve(lower, upper)
    for p_i in primes:
        if p_i >= lower and p_i <= upper: 
            print(p_i)
    print("")
