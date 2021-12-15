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
#%% 프로그래머스 2단계 (더맵게) - 힙 @효율성 0점 
import heapq
def solution(scoville, K):
    answer = 0
    heap = scoville
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + int(b * 2))
        print(heap)
print(solution([1, 2, 3, 9, 10, 12],7))
#%% 프로그래머스 2단계 (타겟넘버) - 깊이너비
#%% 프로그래머스 2단계 (가장큰수) - 정렬 @효율성 0점
def solution(numbers):
    answer = ''
    s_num = numbers.copy()
    n_len = int('1' * len(str(max(numbers))))

    for i in range(len(s_num)):
        if len(str(s_num[i])) < len(str(max(s_num))):
            s_num[i] *= n_len
    
    s_num = sorted(s_num)
    print(s_num)
    while s_num:
        j = s_num.pop()
        if s_num and int(j / n_len) == int(s_num[-1] / n_len):
            answer += str(max(j, s_num[-1]))
        else:
            if int(j / n_len) in numbers:
                answer += str(int(j / n_len))
            else:
                answer += str(int(j))

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
