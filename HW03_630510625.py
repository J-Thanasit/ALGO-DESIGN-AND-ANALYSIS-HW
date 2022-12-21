n, m = map(int, input().split()) 
if(n >= 1 and m <= 90):
    count = []
    for i in range(n + 1):
        count.append(0)
    count[0] = 0
    for i in range(1, n + 1):
        if (i > m):
            count[i] = count[i-1] + count[i-m]
        elif (i < m or i == 1):
            count[i] = 1
        else:
            count[i] = 2
print(count[n])

