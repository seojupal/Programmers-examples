'''
인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.
'''

### recursive ver.
# def solution(n):

#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return solution(n-1) + solution(n-2)

def solution_recur(n):
    
    if n<2: return n
    else:
        return solution_recur(n-1) + solution_recur(n-2)


### iterative ver.
def solution_iter(n):

    f0 = 0
    f1 = 1

    if n<=1:
        answer = n

    else:
        for i in range(2, n+1):

            answer = f0 + f1

            f0 = f1
            f1 = answer

    return answer



# ------- #
# print(solution_recur(int(input('x: '))))
print(solution_iter(int(input('x: '))))


'''
적용
- 재귀/반복 알고리즘 개념에 대해 어렴풋이 이해가 됐다.
- 중복되는 부분을 줄이고, 코드를 간결하게 쓰는 연습이 필요하다.

알게 된 아이디어
- n=0일 때 0, n=1일 때 1 => n<=1일 때 n으로 통합될 수 있다.
- 한 줄 if문 요약하기

'''