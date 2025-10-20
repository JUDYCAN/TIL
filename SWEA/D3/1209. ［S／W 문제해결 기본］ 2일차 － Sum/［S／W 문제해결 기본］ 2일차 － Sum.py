for _ in range(10):
    N = 100
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = []
    for i in range(N):
        cnt = 0
        dnt = 0
        for j in range(N):
            cnt += arr[i][j]
            dnt += arr[j][i]
        ans.append(cnt)
        ans.append(dnt)

    a = max(ans)

    ant = 0
    bnt = 0
    for i in range(N):
        ant += arr[i][i]
        bnt += arr[i][N-1-i]

    c = max(ant,bnt)

    print(f'#{tc}', max(a,c))