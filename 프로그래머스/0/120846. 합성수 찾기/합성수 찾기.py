def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(2,i):
            if i % j ==0:
                answer +=1
                break
   
    return answer