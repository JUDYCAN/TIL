T = int(input())
for tc in range(T):
    N,P = map(str,input().split())
    P = int(P)
    arr = input().split()

    my_dict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }

    ans = []
    for i in arr:
        if i in my_dict:
            ans.append(my_dict[i])

    ans.sort()

    your_dict = {
        0: "ZRO",
        1: "ONE",
        2: "TWO",
        3: "THR",
        4: "FOR",
        5: "FIV",
        6: "SIX",
        7: "SVN",
        8: "EGT",
        9: "NIN"
    }

    result = []
    for i in ans:
        if i in your_dict:
            result.append(your_dict[i])
    print(N)
    print(*result)