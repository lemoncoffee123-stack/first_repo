T = int(input())

def queen(num):
    global cnt
    if num == N:
        cnt += 1
        return cnt

    for i in range(N):
        if not check_col[i] and not check_dia[num + i] and not check_revdia[i - num + N]:
            check_col[i] = True
            check_dia[num + i] = True
            check_revdia[i - num + N] = True

            queen(num + 1)

            check_col[i] = False
            check_dia[num + i] = False
            check_revdia[i - num + N] = False


for tc in range(1, T + 1):
    N = int(input())
    check_row = [0] * N
    check_col = [0] * N
    check_dia = [0] * (2 * N)
    check_revdia = [0] * (2 * N)

    cnt= 0

    queen(0)

    print(f"#{tc} {cnt}")