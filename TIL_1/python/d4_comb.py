# idx : idx 번째 요소에 대해서 조합 포함여부 결정하기
# cnt : 여태까지 선택한 요소 개수
def comb(idx, cnt):
    # 원하는 개수 만큼의 요소 선택 완료(조합 완성)
    if cnt == M:
        print(bit)
        return
    # 원하는 개수 만큼 요소 선택 못함

    if idx == N:          # 만약 idx가 N까지 도달하면
        return            # 아무것도 안하는걸 return

    # 아래쪽에 인덱스가 남아있으면 선택하면 되지만
        # 만약에 인덱스가 남아있지 않으면 error이므로 10번을 넣어야함
    bit[idx] = 1                # idx번의 요소를 조합에 ㅍ함시킨다
    comb(idx + 1, cnt + 1)

    bit[idx] = 1
    comb(idx + 1, cnt)




# comb_arr 조합 요소 채워넣기, idx번째 요소
# 선택 가능 범위
def comb2(comb_arr, idx, s):
    if idx == M:
        print(comb_arr)
        return

    # comb_arr[idx] = 내가 넣을 수 있는거 다 넣어보기
    for i in range(s, N - M + idx + 1):
        comb_arr[idx] = arr[i]
        comb2(comb_arr, idx+1, i+1)

arr = [1,2,3,4,5,6,7,8]
N = len(arr)
M = 3       #조합 요소 개수
bit = [0] * N
comb2([0]*M, 0, 0)