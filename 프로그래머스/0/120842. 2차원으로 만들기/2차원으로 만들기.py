def solution(num_list, n):
    answer = []
    array=list(range(0,len(num_list),n))
    
    for i in array:
        answer.append(num_list[i:n+i])

    return answer