### 완전 탐색에서 중요한 건 순열이나 조합이냐...
### 1. 경우의 수 계산 — N이 얼마인지 보고, 전부 시도해도 시간 안에 될지 판단
### 2. 구현 방법 선택 — 단순 반복이면 for 중첩, 선택/조합이면 재귀 또는 itertools
### 3. 정답 조건 체크 — 각 경우에서 조건을 만족하는지 확인

def solution(sizes):
    widths = []
    heights = []
    ### 긴 쪽을 가로, 짧은 쪽을 가로로 통일했을 때, 값이 최소인 것을 선택
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0] # 정렬
    
    widths = [sizes[i][0] for i in range(len(sizes))]
    heights = [sizes[i][1] for i in range(len(sizes))]
            
    answer = max(widths) * max(heights)
    return answer