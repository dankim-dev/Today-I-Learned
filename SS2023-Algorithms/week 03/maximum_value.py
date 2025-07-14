def find_max( A ):
    max = 0
    for a in A[1:]: # 0번째가 max면 바로 return이니까, 1번째부터 끝까지 검사
        if a > max:
            max = a
    return max

array = [int(n) for n in input().split()] # 공백으로 구분되는 리스트 입력 받기

print(array, "최댓값은 = ", find_max(array))