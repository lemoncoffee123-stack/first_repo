import sys
input = sys.stdin.readline

N = int(input().strip())
table = list(map(int, input().split()))
size = int(N ** 0.5)
cnt = [0] * 1000001
dist_cnt = [0] * (N + 1)
bucket = [0] * (N//size + 1)

for i in table:
    cnt[i] += 1

for val in cnt:
    if val > 0:
        dist_cnt[val] += 1

for i in range(1, N + 1):
    bucket[i // size] += dist_cnt[i]

M = int(input().strip())
for _ in range(M):
    a, b = map(int, input().split())
    count = 0

    left, right = a, b
    while a <= b and a % size != 0:
        count +=