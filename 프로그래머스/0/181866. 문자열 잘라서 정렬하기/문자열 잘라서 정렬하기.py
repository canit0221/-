def solution(myString):
    answer = myString.split('x')
    answer = [i for i in answer if not i == ""]   
    answer.sort()
    return answer