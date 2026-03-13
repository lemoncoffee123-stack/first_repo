T = int(input())

for tc in range(1, T + 1):
    day, month, q_year, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = dp[i - 1] + min(day * plan[i - 1], month)

        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + q_year)

        elif i < 3:
            dp[i] = min(dp[i], q_year)
    cnt = min(dp[12], year)

    print(f"#{tc} {cnt}")