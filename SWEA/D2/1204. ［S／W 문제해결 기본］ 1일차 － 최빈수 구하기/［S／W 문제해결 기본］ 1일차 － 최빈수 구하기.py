T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))

    zero = [0] * 101

    max_count = 0
    max_idx = 0
    for i in arr:
        zero[i] += 1
    for k in range(101):
        if max_count <= zero[k]:
            max_count = zero[k]
            max_idx = k
        
    
        
    print(f"#{tc} {max_idx}")