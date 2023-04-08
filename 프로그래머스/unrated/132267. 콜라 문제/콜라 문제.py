def solution(a, b, n):
    coke = 0
    while n >= a:
        new = n // a * b
        coke += new
        empty = n % a
        n = new + empty
    return coke
    