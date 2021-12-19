"""
공장의 비용문제로 두개의 조립라인이 하나의 부품공급라인을 공유한다.

부품라인은 두개의 조립라인에 부품을 조립순서대로 공급해 준다.

부품 중 각각의 조립라인에 중복되는 부품은 단 1개만 존재한다.

아래 그림과 같이 부품라인 순서대로 양쪽 조립라인에 부품을 조달할 수 있으며, 모든 부품이 조달되면 정상적으로 조립이 된다.
두 조립라인 모두 성공적으로 조립이 되면 ‘1’ , 조립되지 않으면 ‘0’을 출력하라.

[제약조건]

-조립라인의 부품수는 50개를 넘기지 않는다.

-부품번호는 1=< N =< 100

-각 조립라인에 중복되는 부품은 단 1개 존재한다.
"""
#%% 코딩테스트 
def main(n, arr):
    answer = ['#'] * len(arr)
    up = [0] * len(arr)
    down = [0] * len(arr)
    com_n = [0] * len(arr)

    for i in range(len(arr)):
        sorted(arr[i])
        arr[i].reverse()
        com_n[i] += arr[i][-1]
    
    for i in range(len(arr)):
        if com_n[i] % 2 == 1 or com_n[i] % 10 == 0:
            while arr[i]:
                j = arr[i].pop()
                if len(arr[i]) == 0:
                    break
                if arr[i][-1] == n: #예외처리
                    arr[i].pop()
                if arr[i] and j + com_n[i] == arr[i][-1]:
                    com_n[i] += 1
                    up[i] += 1
                    continue
                else:
                    break
        else:
            count = 1
            while arr[i]:
                j = arr[i].pop()
                if len(arr[i]) == 0:
                    break
                if arr[i][-1] == n: #예외처리
                    arr[i].pop()
                if arr[i] and j + com_n[i] == arr[i][-1]:
                    if count % 2 == 0:
                        com_n[i] += -1
                    com_n[i] += 2
                    down[i] += 1
                    continue
                else:
                    break

    for i in range(len(arr)):
        if (up[i] and down[i] == False) or (down[i] and up[i] == False):
            answer[i] += str(i+1) + ' 1'
        else:
            answer[i] += str(i+1) + ' 0'

    return answer

if __name__ == '__main__':
    arr = [[3, 5, 6, 10, 15],
          [2, 4, 5, 8, 13],
          [2, 3, 4, 5, 6, 5, 8, 10, 13, 15]]
    n = 5
    
    for i in main(n, arr):
        print(i)
 