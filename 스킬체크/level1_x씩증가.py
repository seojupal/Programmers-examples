'''
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

입출력 예
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
'''

def solution(x, n):
    answer = []
    # answer.append(x)

    # if x==0 or n==1:
    #     return [x]
    # else:
    #     tmp = x

    #     for _ in range(1, n):
    #         tmp += x
    #         answer.append(tmp)

    for i in range(n):
        answer.append(x*(i+1))


    return answer

x = -1
n = 10
print(solution(x, n))

'''
적용

테스트 케이스 하나가 안풀려서, 검색해서 결국 답을 봤다.
        answer.append(x*(i+1))
근데 이 라인이 답이 되는지 좀더 고민해보고 자야겠다.
''' 