def solution(answers):
    count1,count2,count3 = 0,0,0 # 맞춘 정답 저장 변수
    p1 = [1, 2, 3, 4, 5] # 수포자1
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] #수포자2
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #수포자3
    answer = []
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            count1 +=1
        if answers[i] == p2[i % len(p2)]:
            count2+=1
        if answers[i] == p3[i % len(p3)]:
            count3 +=1
            
    counts = [count1,count2,count3]
    
    for i,count in enumerate(counts):
        if max(counts) == count:
            answer.append(i+1)
    
    return answer