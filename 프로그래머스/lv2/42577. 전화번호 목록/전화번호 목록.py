def solution(phone_book):
    D = {}
    for x in phone_book:
        D[x] = 0
    for x in D:
        for i in range(len(x)):
            if (x[:i] in D):
                return False
    return True