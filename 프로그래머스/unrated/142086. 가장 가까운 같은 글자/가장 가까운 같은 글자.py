def solution(s):
    # obj = {'a':1, 'b':2}
    # print(obj['a'])
    # obj['c'] = 3
    # print(obj.get('d'))
    
    dict = {}
    answer = []
    for x in range(len(s)):
        if dict.get(s[x]) is None:
            dict[s[x]] = x # dict['b'] = 0
            answer.append(-1)
        else:
            answer.append(x - dict[s[x]])
            dict[s[x]] = x
    
    return answer