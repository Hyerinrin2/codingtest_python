###participant를 순회하면서 이름별 등장 횟수를 카운트
###completion을 순회하면서 카운트를 차감
### 마지막에 카운트가 0이 아닌 이름이 정답

def solution(participant, completion):
    answer = ''
    count = {} ### 등장횟수를 카운트할 딕셔너리
    
    for i in participant:
        try:
            count[i] += 1
        except:
            count[i] = 1
            
    for i in completion:
        try:
            count[i] -= 1
        except:
            count[i] -= 1
    
    for k,v in count.items():
        if v != 0:
            answer = k
    
            
    return answer