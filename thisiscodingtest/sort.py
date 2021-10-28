'''
2021.10.20
[이것이 코딩테스트다] p.178 위에서 아래로
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는프로그램을 만드시오
<입력 예시> <출력 예시>
3          27 15 12
15
27
12
'''

# 내 풀이
n = int(input())
print(n)

data=[]
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

print(data)

# 해설
'''
가장 기본적인 정렬을 할 수 있는지 물어보는 문제. 수의 개수가 500개 이하로 매우 적으며, 모든 수는 1 이상 100,000이하이므로 어떠한 정렬 알고리즘을 사용해도 문제를 해결할 수 있다. 
선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 중 아무거나 이용해도 상관없지만 가장 코드가 간결해지는 파이썬의 기본 정렬 라이브러리를 이용하는 것이 효과적이다.
'''
n = int(input())
print(n)

data=[]
for i in range(n):
    data.append(int(input()))

array = sorted(data, reverse=True)

for i in array:
    print(i, end= '')


'''
2021.10.20
[이것이 코딩테스트다] p.180 성적이 낮은 순서로 학생 출력하기
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오
'''
# 내 풀이
n = int(input())

data = []
result = []
for i in range(n):
    data.append(list(map(str, input().split())))
    if len(data)>1:
        print(int(data[i][1]), int(data[i-1][1]))
        if(int(data[i][1])>int(data[i-1][1])):
            data[i], data[i-1] = data[i-1], data[i]
            
for k in data:
    result.append(k[0])
    
print(result)

# 해설
'''
이 문제는 학생의 정보가 최대 100,000개까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나 O(N)을 보장하는 개수 정렬을 이용하면 된다.
* 나는 sorted key 문법을 몰라서 더 복잡하게 풀었다. 
'''
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')


'''
2021.10.21
[이것이 코딩테스트다] p.182 두 배열의 원소 교체
두 개의 배열 A, B가 있다. 두 배열은 N개의 원소로 구성되어 있고, 배열의 원소는 모두 자연수이다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
N, K 그리고 배열 A, B 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합을 구하라.
'''
# 내 풀이
# 전체적인 건 맞았지만 B가 A 보다 클 때의 조건을 생각 못함
n, k = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

result=0

list_a.sort()
list_b.sort(reverse=True)
print(list_a)
print(list_b)
print('-------')

for i in range(k):
    list_a[i], list_b[i] = list_b[i], list_a[i]
    
print(list_a)
print(list_b)

print(sum(list_a))

# 해설
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))

