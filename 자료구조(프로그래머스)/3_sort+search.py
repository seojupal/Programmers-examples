'''
리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

예를 들어,
L = [2, 3, 5, 6, 9, 11, 15]
x = 6
의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

또 다른 예로, 추가되면 좋을 것으로 판단한 경우가 있어서 "예시 테스트 케이스" 와 "정확성 테스트 케이스" 를 추가하였습니다.
https://programmers.co.kr/questions/19525
L = [2, 5, 7, 9, 11]
x = 4
로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.

이 연습문제에서는 알고리즘의 효율성도 평가합니다. 만약 순차 (선형) 탐색 알고리즘을 구현하는 경우에는 제한 시간 요구사항을 만족하지 못하여 효율성 테스트 케이스들을 통과하지 못할 수도 있습니다.

참고: (2021년 8월 2일) 아래 질문을 검토하다가 테스트 케이스에
'''

# def solution(L, x):

#     L.sort()
#     answer = -1

#     while L[0]<=L[-1]:

#         middle = int(len(L)/2)

#         if L[middle]==x:
#             answer = middle
#             break
#         elif L[0]==L[middle] and not L[0]==x:
#             answer = -1
#             break

#         else:

#             if L[middle]>x:
#                 L = L[:middle]

#             else:
#                 L = L[middle:]

            
#     return answer

''' 통과된 코드 '''
def solution(L, x):

    lower = 0
    upper = len(L)-1
    
    while lower<=upper:
        middle = (lower+upper)//2

        if L[middle]==x:
            return middle
        
        elif L[middle]<x:
            lower = middle + 1
        
        elif L[middle]>x:
            upper = middle - 1


    return -1


L = [2, 3, 5, 6, 9, 11, 15]
x = 6

answer = solution(L,x)
print(answer)


'''
적용:

알게 된 아이디어
- 별 일 없으면 -1로 리턴 값을 정해두고, 중간에 조건에 맞으면 바로 return
- 인덱스가 답이니까 값 비교 말고는 계속 인덱스를 다룬다 -> 코드 단순해짐
- 빈 리스트가 입력일 때도 고려

질문
- 이진탐색은 리스트가 정렬되어 있다는 게 기본인데, 여기는 반드시 정렬된 리스트를 준다는 조건이 없는 것 같다.
  그럼 sort 등의 코드 안 써도 되는 건가?

'''