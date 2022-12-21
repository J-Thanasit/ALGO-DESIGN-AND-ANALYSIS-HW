N = int(input())
k = int(input())
s = []
a = 0
for i in range(k):
    s.append(int(input()))
s = sorted(s)
s_ = len(s) - 1
while(N > 0):
    if(N >= s[s_]):
        N = N - s[s_]
        a += 1
    else:
        s_ -= 1
print(a)