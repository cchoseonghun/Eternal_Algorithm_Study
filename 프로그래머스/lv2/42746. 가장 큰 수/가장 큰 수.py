def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: x*3, reverse=True)
    result = ''.join(arr)
    if result[0] == '0':
        return '0'
    return result