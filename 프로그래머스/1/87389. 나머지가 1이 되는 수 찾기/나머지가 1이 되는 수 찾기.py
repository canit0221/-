def solution(n):
    answer = 0
    divide = []
    
    for i in range(1,n):
        if n % i == 1:
            answer = i
            break
    return answer