
from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = deque(map(int, input().split()))
    arr2 = deque(map(int, input().split()))
    final_list = []
    if N < M:
        while len(arr1) <= M:
            sumi = 0
            for i in range(len(arr1)):
                sumi += arr1[i] * arr2[i]
            final_list.append(sumi)
            arr1.appendleft(0)
    else:
        while len(arr2) <= N:
            sumi = 0
            for i in range(len(arr2)):
                sumi += arr1[i] * arr2[i]
            final_list.append(sumi)
            arr2.appendleft(0)

    print(f"#{tc} {max(final_list)}")