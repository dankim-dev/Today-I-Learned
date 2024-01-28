# 2차원 평면 상의 n개의 점에서 가장 인접한 쌍의 거리 구하기

import math # 모듈 불러오기
def distance(p1, p2): # 유클리드 거리 구하기
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) # math.sqrt는 제곱근을 구해주므로 마지막에 루트를 없애기 위한 **0.5를 할 필요가 없다.

INF = float('Inf') # 가장 큰 가중치 (실수 무한대)
import sys
INF = sys.maxsize # 가장 큰 가중치 (정수 무한대)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist


n = int(input())
p = [tuple(int(n) for n in input().split()[:2]) for _ in range(n)] 


print("최근접 거리:", closest_pair(p))