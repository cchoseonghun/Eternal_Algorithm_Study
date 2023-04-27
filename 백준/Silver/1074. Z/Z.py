def z(n, r, c):
    if n == 1:
        return 2 * r + c
    h = 2 ** (n - 1)
    if r < h and c < h:
        return z(n - 1, r, c)
    elif r < h and c >= h:
        return h ** 2 + z(n - 1, r, c - h)
    elif r >= h and c < h:
        return 2 * h ** 2 + z(n - 1, r - h, c)
    else:
        return 3 * h ** 2 + z(n - 1, r - h, c - h)

N, r, c = map(int, input().split())
print(z(N, r, c))
