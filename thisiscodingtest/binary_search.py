'''
2021.10.24
[이것이 코딩테스트다] p.197 부품 찾기
동빈이네 전자 매장에는 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서를 욜청했다.
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력한다.
'''
# 내 풀이
n = int(input())
total = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

result = []
for i in check:
    if not i in total:
        result.append('no')
        
    else:
        result.append('yes')

print(result)

# 해설(이진 탐색)
'''
먼저 매장 내 N개의 부품을 번호를 기준으로 정렬하자. 그 이후 M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사하면 된다. 이때 매장의 부품은 정렬되어 있기 때문에 이진탐색을 행할 수 있다.
이렇게 문제를 풀면, 부품을 찾는 과정에서 최악의 경우 시간 복잡도 O(M * logN)의 연산이 필요하므로 이론상 최대 약 200만 번의 연산이 이루어진다고 분석할 수 있다.
오히려 N개의 부품을 정렬하기 위해서 요구되는 시간 복잡도 O(N * logN)이 이론적으로 최대 약 2000만으로 더욱더 많은 연산이 필요한 것을 알 수 있다.
결과적으로 이진 탐색을 사용하는 문제 풀이 방법의 경우 시간 복잡도는 O((M + N) * logN)이다.
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        return None

    # N(가게의 부품 개수) 입력
    n = int(input())
    # 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
    array = list(map(int, input().split()))
    array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
    # M(손님이 확인 요청한 부품 개수) 입력
    m = int(input())
    # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
    x = list(map(int, input().split()))

    # 손님이 확인 요청한 부품 번호를 하나씩 확인
    for i in x:
        # 해당 부품이 존재하는지 확인
        result = binary_search(array, i, 0, n -1)
        if result != None:
            print('yes', end=' ')
        else:
            print('no', end=' ')

# 해설2(계수 정렬)
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 해설3(집합 자료형)
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인하기
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')


'''
2021.10.24
[이것이 코딩테스트다] p.201 떡볶이 떡 만들기
이 떡집은 떡의 길이가 일정하지 않다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 0.2cm이다. 손님은 6cm 만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
<입력 예시>     <출력 예시>
4 6           15
19 15 10 17 
'''

# 내 풀이
# 못품

# 해설
'''
파라메트릭 서치 유형의 문제이다. 파라메트릭 서치는 최대적화 문제를 결졍 문제로 바꾸어 해결하는 기법이다. '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 사용한다.
절단기의 높이(탐색범위)는 1부터 10억까지의 정수 중 하나인데, 이처럼 큰 수를 보면 당연하게 가장 먼저 이진 탐색을 떠올려야 한다.
step1. 
시작점은 0, 끝점은 가장 긴 떡의 길이 19로 설정한다. 0과 19 사이의 중간점 9를 절단기 높이 H로 설정하면 어을 수 있는 떡의 합은 (10+6+1+8)=25이다. 
필요한 떡의 길이가 6보다 크기때문에 시작점을 증가시킨다.
step2.
시작점을 10으로 옮긴다. 끝점은 여전히 19이므로 중간점은 14이다. 절단기 높이를 14로 설정하면 얻을 수 있는 떡의 합이(5+1+3)=9이다. 여전히 필요한 떡의 길이인 6보다 크기 때문에 시작점을 증가시킨다.
step3.
현재 시작점은 15, 끝점은 19, 중간점이 17이므로 얻을 수 있는 떡의 합은 2이다. 필요한 떡의 길이인 6보다 작기 때문에 끝점을 감소시킨다.
step4.
현재 시작점은 15, 끝점은 16, 중간점이 15이므로 얻을 수 있는 떡의 합은 (4+2)=6이다. 필요한 떡의 길이인 6과 동일하다.
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start<=end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result 기록
        start = mid + 1

print(result)