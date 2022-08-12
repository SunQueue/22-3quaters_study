name = "JAZ"
# name = "JEROEN"
#name = "JAN"

def solution(name) : 
#     print(f"name={name}")
#     print(f"len={len(name)}")
    # print(f"A = {ord('A')}") #65
    # print(f"Z = {ord('Z')}") #90
    arr = list(name)
    print(arr)
    sum = 0
    sarr = []
    flag = False
    aCount = 0
    for i in arr :
        if i is not 'A' :
            # print(f"{ord(i)-ord('A'), 91-ord(i)}") 
            sum += min(ord(i)-ord('A'), 91-ord(i))
    
    # print(sum)
    #좌-우로 움직이는 횟수 count = min(count)

    #answer = sum + count 


    answer = 0
    return answer

solution(name)