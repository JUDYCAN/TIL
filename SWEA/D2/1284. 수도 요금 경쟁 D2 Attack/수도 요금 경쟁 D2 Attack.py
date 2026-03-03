T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A_com = P * W
    if W <= R :
        B_com = Q
    elif W > R :
        B_com = Q + ( S * (W-R))

    rate = 0
    if A_com < B_com :
        print(f"#{tc} {A_com}")
    else:
        print(f"#{tc} {B_com}")