## possibleregex = 19682 -> 222222222
## possibleregex with turns 39365 -> 1222222222

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def ternary_to_base10(n):
    strnum = str(n)
    total = 0
    for i in range(len(strnum)):
        total += int(strnum[i])*(3**(len(strnum)-i-1))
    return total

def ternary_adapter(num):
    strnum = ternary(num)
    lenstrnum = len(strnum)
    zeroneeded = 10 - lenstrnum
    strzero = '0'*zeroneeded
    return strzero + strnum
    