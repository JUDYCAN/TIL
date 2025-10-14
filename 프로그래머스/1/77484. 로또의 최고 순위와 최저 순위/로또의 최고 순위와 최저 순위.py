def solution(lottos, win_nums):
    zero = lottos.count(0)
    cnt = 0
    for i in lottos:
        if i != 0 and i in win_nums:
            cnt += 1
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    best = zero + cnt  # 4
    worst = cnt
    return [rank[best],rank[worst]]