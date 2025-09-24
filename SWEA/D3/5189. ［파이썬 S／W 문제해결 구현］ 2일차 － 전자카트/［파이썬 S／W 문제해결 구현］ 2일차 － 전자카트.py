T = int(input())

def electricity(now, cnt, cost):
    global min_cost

    if cost > min_cost:
        return

    if cnt == N - 1:
        min_cost = min(min_cost, cost + arr[now][0])
        return

    for i in range(1, N):
        if visited[i] == 0:
            visited[i] = 1
            #i, cnt+1은 순열을 만드는 행위이다.
            #visited를 활용하여 1, 2, 3 이런 식으로 갔다가 N - 1의 길이에서 그만 돌아가는 것임.
            #i 자체가 순열이고, i를 넣으면 i = now가 되어서 지금있는 곳이 됨.
            electricity(i, cnt + 1, cost + arr[now][i])
            visited[i] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    min_cost = 21e9
    electricity(0, 0, 0)
    print(f"#{tc} {min_cost}")