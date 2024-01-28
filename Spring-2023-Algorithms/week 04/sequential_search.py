def sequential_search(A, key):
    for i in range(len(A)): # A의 길이만큼 반복 (i : 0, 1, ..., len(A)-1)
        if A[i] == key: # key와 동일한 값 나오면
            return i # i 반환
    return -1

A = [int(n) for n in input().split()]
key = int(input())

print("%d찾기 : " %(key), sequential_search(A, key))