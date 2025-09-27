
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    final_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumi = 0
            for di in range(i, i+M):
                for dj in range(j, j+M):
                    sumi += arr[di][dj]
            final_list.append(sumi)
    print(f"#{tc} {max(final_list)}")