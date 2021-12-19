#%% 프로그래머스 1단계 (직사각형 별찍기)
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
#%% 프로그래머스 1단계 (x만큼 간격이 있는 n개의 숫자)
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer
print(solution(2,3))
#%% 프로그래머스 1단계 (행렬의 덧셈)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        line = []
        for j in range(len(arr1[i])):
            line.append(arr1[i][j] + arr2[i][j])
        answer.append(line)
    
    return answer
#%% 프로그래머스 1단계 (핸드폰 번호 가리기)
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if(i < len(phone_number)-4):
            answer += '*'
        else:
            answer += phone_number[i]
    return answer
#%% 프로그래머스 1단계 (하샤드 수)
def solution(x):
    s = sum([int (i) for i in str(x)])
    
    if(x % s == 0):
        return True
    else:
        return False
#%% 프로그래머스 1단계 (평균 구하기)
import statistics
def solution(arr):
    answer = statistics.mean(arr)
    return answer
#%% 프로그래머스 1단계 (콜라츠 추측)
def solution(num):
    answer = 0
    if num >= 8000000:
        return -1
    while 1:
        if num == 1:
            break;
        answer += 1
        if answer > 500:
            return -1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        
    return answer
#%% 프로그래머스 1단계 (최대공약수와 최소공배수)
def solution(n, m):
    answer = []
    x, y = n, m
    
    while(y):
        x, y = y, x % y
    answer.append(x)
    answer.append(n * m // x)
    
    return answer
#%% 프로그래머스 1단계 (짝수와 홀수)
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
#%% 프로그래머스 1단계 (제일 작은 수 제거하기)
def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
    else:
        arr.remove(min(arr))
        answer = arr
    return answer
#%% 프로그래머스 1단계 (정수 제곱근 판별)
import math
def solution(n):
    answer = math.sqrt(n)
    
    if answer == int(answer):
        answer = int(math.pow(answer+1, 2))
    else:
        answer = -1
        
    return answer
#%% 프로그래머스 1단계 (정수 내림차순으로 배치하기)
import math
def solution(n):
    answer = str(n)
    line = []
    
    for i in range(len(answer)):
        line.append(int(answer[i]))
    
    line.sort(reverse=True)
    
    answer = ''

    for i in range(len(line)):
        answer += str(line[i])
        
    return int(answer)
#%% 프로그래머스 1단계 (자연수 뒤집어 배열로 만들기)
def solution(n):
    answer = []
    line = str(n)
    
    for i in range(len(line)):
        answer.append(int(line[len(line) - (i+1)]))
    return answer
#%% 프로그래머스 1단계 (자릿수 더하기)
def solution(n):
    answer = 0
    s = str(n)
    for i in range(len(s)):
        answer += int(s[i])
    
    return answer
#%% 프로그래머스 1단계 (이상한 문자 만들기)
def solution(s):
    answer = ''
    line = s.split(' ')
    
    for i in range(len(line)):
        s = line[i]
        for j in range(len(s)):
            if j % 2 == 0: 
                answer += s[j].upper()
            else: 
                answer += s[j].lower()
                
        if i != len(line) - 1:
            answer += ' '
            
    return answer
#%% 프로그래머스 1단계 (체육복)
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)
    
print(solution(5, [2, 4], [1, 3, 5]))

#%% 프로그래머스 1단계 (K번째수)
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]:])[commands[i][2]-1])
    return answer

print (solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#%% 프로그래머스 1단계 (완주하지 못한 선수)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ""
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    if answer == "":
        answer = participant[-1]
        
    return answer
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

#%% 프로그래머스 1단계 (수포자)
def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_count = 0
    b_count = 0
    c_count = 0

    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            a_count += 1
        if b[i%8] == answers[i]:
            b_count += 1
        if c[i%10] == answers[i]:
            c_count += 1
    
    score = [a_count, b_count, c_count]
    maxscore = max(score)
    
    for i in range(len(score)):
        if score[i] == maxscore:
            answer.append(i+1)
    
    return answer

print(solution([1,3,2,4,2]))
#%%