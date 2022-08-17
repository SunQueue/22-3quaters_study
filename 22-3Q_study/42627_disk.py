input = [[0,3],[1,9],[2,6]]

def solution(jobs):
    jobs.sort(key=lambda x : (x[1], x[0]))#수행시간(x[1]) 짧은 순으로 정렬 후 대기 순서(x[0]) 짧은 순으로 정렬
    # print(jobs)
    indivSum = 0
    totSum = 0
    # print(f"len={len(jobs)}")
    elements = len(jobs)
    while jobs :
        
        indivSum += jobs[0][0]
        # print(f"indivSum={indivSum}")
        # print(f"jobs[0][1] = {jobs[0][1]}")
        
        totSum += (indivSum - jobs[0][0])
        # print(f"jobs[0][0] = {jobs[0][0]}")
        # print(f"totSum={totSum}")
        jobs.pop(0)
        # print(f"jobs={jobs}")

    answer = totSum//elements
    return answer

solution(input)
