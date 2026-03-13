T = int(input())


def dfs(num, cnt, number):  # 함수의 인자 1. 부분집합에 들어가는 수의 갯수 2. 부분집합의 합 3. 지금 고를 숫자
    global count
    if num == N:  # 부분집합의 수가 N가 되었을 때
        if cnt == K:  # 부분 집합의 합이 K가 되었을 때
            count += 1
        return  # if 문을 하나로 합치면 num == N인 경우가 생략이 되면서 무한루프가 될 수 있음!

    if cnt >= K:  # 가지치기 cnt(부분집합의 합)이 K보다 같거나 크면 최종 합이 무조건 K 보다 크므로 의미없음!
        return

    for i in range(number, 13):  # 지금 고를 수 있는 숫자를 고른다
        if not visited[i]:  # 그리고 그 숫자가 방문하지 않았을 때!
            visited[i] = True  # 방문처리
            dfs(num + 1, cnt + i, i + 1)  # 다음 함수 호출
            # 부분집합 개수, 집합의 합, 다음에 시작할 숫자
            visited[i] = False  # 다시 돌아왔을 때, 방문처리 취소! 그래야 다음 반복에서 다시 방문이 가능함!


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0
    visited = [False] * 13
    dfs(0, 0, 1)
    print(f"#{tc} {count}")