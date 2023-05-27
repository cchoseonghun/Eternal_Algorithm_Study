def solution(myString):
    arr = myString.split('x')
    return [len(x) for x in arr]
