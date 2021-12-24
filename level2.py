#%% 프로그래머스 2단계 (피보나치)
def solution(n):
    line = [0, 1]
    for i in range(2, n + 1):
        line.append((line[i - 2] + line[i - 1])%1234567)
    return line[-1]
print(solution(3))
#%% 프로그래머스 2단계 (최솟값 만들기)
def solution(A,B):
    answer = 0
    s_A = sorted(A)
    s_B = sorted(B)
    for i in range(len(A)):
        answer += s_A[i] * s_B[-(i + 1)]
    return answer

print(solution([1, 4, 2], [4, 5, 4]))
#%% 프로그래머스 2단계 (최대값과 최소값)
def solution(s):
    st = sorted(s.split(' '))
    st = list(map(int, st))
    return str(min(st)) + ' ' + str(max(st))

print(solution("-1 -2 -3 -4"))
#%% 프로그래머스 2단계 (숫자의 표현)
def solution(n):
    answer = 1 #자기자신 카운트 
    
    for i in range(1, n):
        a, b = i, i + 1
        for j in range(n - i):
            if a == n:
                answer += 1
                break
            elif a > n:
                break
            else:   
                a, b = a + b, b + 1
    return answer
print(solution(15))
#%% 프로그래머스 2단계 (다음 큰 숫자)

def solution(n):
    a = str(bin(n)).count('1')
    i = 1
    while True:
        if str(bin(n+i)).count('1') == a:
            return n+i
        else:
            i += 1
print(solution(78))

#%% 프로그래머스 2단계 (전화번호목록) - 해시
def solution(phone_book):
    set_ph = sorted(list(map(str, set(phone_book))))    #정렬

    for i in range(len(set_ph) - 1):                      #arr의 2번째부터 n 만큼 반복
        if len(set_ph[i]) < len(set_ph[i + 1]):                 #현재 index의 len이 다음 index len보다 클때 탈출
            if set_ph[i] in set_ph[i + 1][:len(set_ph[i])]:   #현재 index의 값이 다음 인덱스의 포함되어있으면 return f
                return False
                
    return True
print(solution(["119", "97674223", "1195524421"]))
#%% 프로그래머스 2단계 (기능개발) - 스택큐
def solution(progresses, speeds):
    answer = []
    queue = [0] * len(progresses)
    for i in range(len(progresses)):
        while progresses[i] < 100:
            queue[i] += 1
            progresses[i] += speeds[i]
    print(queue)
    queue.reverse()         #숫자 뒤집어주기
    while queue:
        answer.append(1)    #첫번째는 무조건 +1
        j = queue.pop()
        while queue and j >= queue[-1]: #큐가 비어있지 않고 현재의 값이 그 다음값보다 클때 수행
            answer[-1] += 1
            queue.pop()
    return answer
print(solution([93, 30, 55], [1, 30, 5]))  
#%% 프로그래머스 2단계 (프린터) - 스택큐
#%% 프로그래머스 2단계 (더맵게) - 힙
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] > K:
            return answer
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1

    return -1
print(solution([3, 2, 1, 9, 10, 12],7))
#%% 프로그래머스 2단계 (타겟넘버) - 깊이너비
#%% 프로그래머스 2단계 (가장큰수) - 정렬
def solution(numbers):
    answer = ''
    line = []
    
    sum_ = sum(numbers)
    if sum_ == 0:
        return '0'
    
    for i in range(len(numbers)):
        line.append([str(numbers[i])*4, len(str(numbers[i]))])
    
    line.sort()
    
    for i in range(len(line)):
        j = line.pop()
        answer += j[0][:j[1]]
    
    return answer
print(solution([1, 10, 100, 1000]))
#%% 프로그래머스 2단계 (위장) - 해시
#%% 프로그래머스 2단계 (H-index) - 정렬


#%% 프로그래머스 2단계 (다리를지나는트럭) - 스택큐
#%% 프로그래머스 2단계 (주식가격) - 스택큐
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer
print(solution([1,2,3,2,3]))
#%% 프로그래머스 2단계 (행렬 테두리 회전하기)
def solution(rows, columns, queries):
    answer = []
    arr = []
    #init
    for i in range(1, rows * columns + 1, +columns):
        line = []
        for j in range(columns):
            line.append(i + j)
        arr.append(line)

    for i in range(len(queries)):
        if i == 0 and queries[i][2] == rows and queries[i][3] == columns:
            answer.append(1)
            continue
        min_ = [];
        a = arr[queries[i][0] - 1][queries[i][1] - 1] #왼쪽 위 값 저장
        #왼쪽 변경
        for j in range(queries[i][0] - 1, queries[i][2] - 1):
            arr[j][queries[i][1] - 1] = arr[j + 1][queries[i][1] - 1]
            min_.append(arr[j][queries[i][1] - 1])
        #아래 변경
        for j in range(queries[i][1] - 1, queries[i][3] - 1):
            arr[queries[i][2] - 1][j] = arr[queries[i][2] - 1][j + 1]
            min_.append(arr[queries[i][2] - 1][j])
        # #오른쪽 변경
        for j in range(queries[i][2] - 1, queries[i][0] - 1, -1):
            arr[j][queries[i][3] - 1] = arr[j - 1][queries[i][3] - 1]
            min_.append(arr[j][queries[i][3] - 1])
        # #위 변경
        for j in range(queries[i][3], queries[i][1], -1):
            arr[queries[i][0] - 1][j - 1] = arr[queries[i][0] - 1][j - 2]
            min_.append(arr[queries[i][0] - 1][j - 1])
            if j - 1 == queries[i][1]:
                arr[queries[i][0] - 1][j - 1] = a
                min_.append(a)
        answer.append(min(min_))
    return answer
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#%%