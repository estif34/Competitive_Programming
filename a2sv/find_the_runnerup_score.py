if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res = list(arr)
    res.sort(reverse=True)
    for i in res:
        if i < max(res):
            print(i)
            break