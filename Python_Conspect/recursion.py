def fac(n: int) -> int:
    if not isinstance(n, int):
        return -1

    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return n * fac(n - 1)

for i in range(0, 11):
    print(fac(i))
    
print(fac(2.5))
    

def fibo (n: int) -> int:
    if not isinstance(n, int) or n < 1:
        return []
    
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    result = [0, 1]
    n -= 2
    while n > 0:
        n -= 1
        result.append(result[-2] + result[-1])
    
    
    return result
    
    
print(fibo(7))