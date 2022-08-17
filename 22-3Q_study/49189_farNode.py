n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    edge.sort(key=lambda x : (x[0], x[1]))
    arr = [[] for _ in range(n+1)]
    flag = [True for _ in range(n+1)]
    
    for i in edge :
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    
    depth = 0
    maxDepth = 0
    count = 0
    q = []
    q.append(1)
    
    while q : 
        if flag[q[0]] is True : 
            q += arr[q[0]]
            depth += 1
            arr.pop(q[0])
            flag[q[0]] = False
            q.pop(0)
        else :
            q.pop(0)

    answer = 0
    return answer

solution(n, edge)