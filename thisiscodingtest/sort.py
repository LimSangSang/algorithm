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
