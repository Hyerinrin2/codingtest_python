# 최소값을 구하기 위해선 가장 큰 값부터 빼버리면 됨
# 덧셈 연산자 -> 뺄셈 연산자
answer=0
a = list(map(str, input().split("-")))

#  덧셈
def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum+=int(i)
    return sum


for i in range(len(a)):
    temp = mySum(a[i])
    if i==0: # 첫번째 값
        answer+=temp
    else:
        answer-=temp
print(answer)
