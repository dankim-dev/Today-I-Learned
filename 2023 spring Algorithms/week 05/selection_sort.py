# 리스트의 오름차순 정렬 (선택 정렬)
def selection_sort(A):
    n = len(A)
    for i in range(n-1): # 리스트의 마지막은 자동으로 정렬되니 n-1까지
        least = i # 첫 루프의 시작 인덱스를 최솟값으로 일단 설정
        for j in range(i+1, n): # i+1부터 끝까지 반복
            if (A[j] < A[least]): # 앞 최솟값 (least)보다 작은 값이 있으면
                least = j # least값 갱신
        A[i], A[least] = A[least], A[i] # swap
        printStep(A, i+1) # 현재 정렬된 리스트와 단계 (i + 1) 출력

def printStep(arr, val):
    print("  Step %2d = " %val, end='') # &2d : 문자열 formatting 2만큼 길이 가지며 빈 공간은 공백으로 두고 오른쪽 정렬해 출력, end=''를 통해 step과 val 리스트가 공백 없이 이어지게 함
    print(arr)
        
A = [int(n) for n in input().split()] 

print("Original  :", A)
selection_sort(A)
print("Selection :", A)