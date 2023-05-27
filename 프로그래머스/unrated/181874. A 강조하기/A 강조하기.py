def solution(myString):
    answer = ''
    for x in myString:
        if x == 'a':
            answer += 'A'
        elif x != 'A' and x != ' ' and ord(x) < ord('a'):
            answer += chr(ord(x) + ord('a') - ord('A'))
        else:
            answer += x
    return answer