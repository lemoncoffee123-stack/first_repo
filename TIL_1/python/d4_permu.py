# 순열(permutation)
# perm_arr의 idx 번째 요소 고르기

def perm(perm_arr,idx):
    if idx == N:
        print(perm_arr)
        return


    # perm_arr[idx] = 에 아직 사용안한거 다 넣기
    for i in range(N):
        if not check[i]:
            perm_arr[idx] = arr[i]
            check[i] = 1
            perm(perm_arr,idx + 1)          # 다음 숫자 고르러 가기
            check[i] = 0



arr = [1,2,3]
N = len(arr)
check = [0] * N     # 요소 중복선택 방지
perm([0]*N, 0)