### 최대 n의 횟수가 100,000인데 구간마다 합을 구하면 0.5초 안에 못 끝내서 시간초과
### --> 이때 구간합 사용
### 1. n개의 수를 입력받음과 동시게 합 배열 생성
### 2. 구간 합 도출

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split()) # 숫자개수,질의개수
numbers = list(map(int, input().split())) # 숫자 데이터 생성
prefix_sum = [0] #합 배열 선언
temp = 0

for i in numbers: # 합 배열 생성
    temp += i
    prefix_sum.append(temp)
    
for i in range(quizNo): # 합 배열에서 구간 합 구하기
    s,e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

