""" 
0 또는 양의 정수가 주어졌을 때,
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 
return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330" 
"""
from itertools import permutations
from functools import cmp_to_key

# permutation을 통해 모든 경우의 수를 순열로 모두 찾다 보니 시간복잡도가 o(n*n!)
# 이렇게 풀면 시간초과로 못 품
def solution(numbers):
    answer = ''

    new_num = permutations(numbers)
    for i in new_num:
        join_num = ''.join(map(str,i))
        answer.append(join_num)

    return max(answer)

def lambda_solution(numbers):
    return max(list(map(lambda x:''.join(map(str,x)),permutations(numbers))))


# 기준을 정해서 정렬을 먼저하고 찾는 게 핵심
def real_solution(numbers):
    # 1. 숫자를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. 비교함수 정의
    def compare(x, y):
        # x+y와 y+x 중 더 큰 것을 앞으로 오게 함
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # 3. 정렬
    numbers.sort(key=cmp_to_key(compare))

    # 4. 모두 0일 때 예외처리
    if numbers[0] == '0':
        return '0'

    # 5. 정렬된 숫자를 이어 붙여 결과 반환
    return print(''.join(numbers))

""" 다른 사람 풀이 """
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


if __name__=="__main__":
    numbers = [6, 10, 2]
    # solution(numbers)
    # print(lambda_solution(numbers))
    real_solution(numbers)