words = ["G...", ".I.T", "..S."]

K = int(input())
result = []

for i in range(3):
    word = ""
    for j in range(4):
        for _ in range(K):
            word += words[i][j]
    for _ in range(K):
        result.append(word)

print(*result, sep="\n")