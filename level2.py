#%% 프로그래머스 2단계 (전화번호목록)
def solution(phone_book):
    set_ph = sorted(list(map(str, set(phone_book))))    #정렬

    for i in range(len(set_ph) - 1):                      #arr의 2번째부터 n 만큼 반복
        if len(set_ph[i]) < len(set_ph[i + 1]):                 #현재 index의 len이 다음 index len보다 클때 탈출
            if set_ph[i] in set_ph[i + 1][:len(set_ph[i])]:   #현재 index의 값이 다음 인덱스의 포함되어있으면 return f
                return False
                
    return True
print(solution(["119", "97674223", "1195524421"]))
#%% 프로그래머스 2단계 (기능개발)
def solution(progresses, speeds):
    answer = []
    return answer
print(solution([93, 30, 55], [1, 30, 5]))  
#%% 프로그래머스 2단계 (프린터) - 스택큐
#%% 프로그래머스 2단계 (더맵게) - 스택큐
#%% 프로그래머스 2단계 (타겟넘버) - 힙
#%% 프로그래머스 2단계 (가장큰수) - 깊이너비
#%% 프로그래머스 2단계 (위장) - 정렬
#%% 프로그래머스 2단계 (H-index) - 해시
#%% 프로그래머스 2단계 (다리를지나는트럭) - 스택큐
#%% 프로그래머스 2단계 (주식가격) - 스택큐
def solution(prices):
    answer = []
    if len(prices) < 2 and len(prices) > 100000:
        return -1
    
    for i in range(len(prices)):
        count = 0
        j = i + 1
        while j < len(prices):
            if prices[i] <= prices[j]:
                count += 1
                j += 1
            elif prices.index(prices[i]) + 1 <= len(prices):
                count += 1
                break
            else:
                break            
        answer.append(count)
    return answer
print(solution([1,2,3,2,3]))
#%%[3, 1, 1, 2, 1, 0]    [5, 8, 6, 2, 4, 1]