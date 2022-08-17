name = "JAZ"
# name = "JEROEN"
# name = "JAN"
def solution(name) : 
    arr = list(name)
    print(arr)
    sum = 0
    mid = []
    aCount = 0
    ans = 0

    for i in range(len(arr)) :
        if arr[i] == 'A' : 
            if i == (len(arr)-1) or arr[i+1] != 'A' :
                aCount += 1
                mid.append(aCount)
                aCount = 0
            else: 
                aCount += 1
        else :
            if i == (len(arr)-1) or arr[i+1] == 'A' :
                sum += min(ord(arr[i])-ord('A'), 91-ord(arr[i]))
                mid.append(sum)
                sum = 0    
            else: 
                sum += min(ord(arr[i])-ord('A'), 91-ord(arr[i]))

    if len(mid) == 1 : #no 'A'
        ans = mid[0] + len(arr) - 1
        return ans

    if len(mid)%2 == 1:
        mid.append(1)        
    print(mid)

    while len(mid)>1 : 
        if mid[1] >= mid[-1]: #go Back
            ans += (mid[0] + mid[-1] + mid[-2])
            mid.pop(0)
            mid.pop()
            mid.pop()
        else : #go Front
            ans += (mid[0]+ mid[1] + mid[2])
            mid.pop(0)
            mid.pop(0)
            mid.pop(0)

    answer = ans
    return answer

print(solution(name))
