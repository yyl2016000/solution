n, t, c = list(map(int, input().split()))
in_list = list(map(int, input().split()))
in_list.append(t + 1)

i, j = 0, 0
res = 0
while i < n and j < n: 
    while i < n and in_list[i] > t: 
        i += 1
    j = i + 1
    while j < n and in_list[j] <= t: 
        j += 1
    tmp = j - i - c + 1
    if tmp > 0: 
        res += tmp
    i = j + 1
    j = i + 1
print(res)