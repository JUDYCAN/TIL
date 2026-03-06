T = int(input())

for tc in range(1, T+1):
    arr = (str(input()))
    len_arr = len(arr)
    middle = len_arr // 2

    left = arr[:middle]
    right = arr[middle+1:]

    if arr == arr[::-1] and left == left[::-1] and right == right[::-1]:
        print(f"#{tc} YES")
    else :
        print(f"#{tc} NO")