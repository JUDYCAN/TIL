
T = int(input())

def minsum(row, final):
    global min_final
    #가지치기
    if min_final <= final:
        return

    #종료조건
    if row == N:
        min_final = min(min_final, final)
        return

    #재귀
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            minsum(row+1, final + arr[row][i])
            visited[i] = 0




for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_final = 9999
    minsum(0,0)
    print(f"#{tc} {min_final}")