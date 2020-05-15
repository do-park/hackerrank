# Day 6: Let's Review

N = int(input())
for n in range(N):
    S = input()
    odd = []
    even = []
    for s in range(len(S)):
        if s & 1:
            odd.append(S[s])
        else:
            even.append(S[s])
    print(''.join(even), end=' ')
    print(''.join(odd))
