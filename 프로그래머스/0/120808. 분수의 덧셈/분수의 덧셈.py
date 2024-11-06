def gcd(a,b):
    r = a%b
    if r==0:
        return b
    return gcd(b, r)

def solution(numer1, denom1, numer2, denom2):
    ans = [(numer1 * denom2) + (numer2 * denom1), denom1 * denom2]
    
    lcm = gcd(ans[0],ans[1])
    return list(map(lambda x: x//lcm, ans))
