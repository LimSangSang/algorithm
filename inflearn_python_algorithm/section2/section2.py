'''
k번 째 약수

어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 6을 예로 들면
6÷1=6...0 
6÷2=3...0 
6÷3=2...0 
6÷4=1...2 
6÷5=1...1 
6÷6=1...0
그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
▣ 입력설명
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
▣ 출력설명
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
▣ 입력예제 1 63
▣ 출력예제 1 3


# 나의 풀이
n, k = map(int, input().split())

arr = []
for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

if k > len(arr):
    print(-1)
else:
    print(arr[k-1])

# 해설
n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n%1 == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
'''
'''
k번째 수

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다. 두 번째 줄에 N개의 숫자가 차례로 주어진다.
▣ 출력설명
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
▣ 입력예제 1 2
6253 527389 15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
▣ 출력예제 1 
#1 7
#2 6


#나의 풀이
t = int(input())

for i in range(1, t+1):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    temp = arr[s-1:e]
    temp.sort()

    print(i, temp[k-1])
'''

'''
k번째 큰 수

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.
▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.
▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
▣ 입력예제 1
10 3
13 15 34 23 45 65 33 11 26 42
▣ 출력예제 1 143

# 내 풀이
# 중복 제거를 틀리게 구현
n, k = map(int, input().split())
arr = list(map(int, input().split()))

total=[]
for ai, a in enumerate(arr):
    print('a > ', a, ai)
    for bi, b in enumerate(arr):
        if (ai != bi):
            print('b > ', b, bi)
        for ci, c in enumerate(arr):
            if (ai != ci or bi != ci):
                print('c > ', c, ci)
                total.append(a+b+c)

total.sort(reverse=True)
print(total[k-1])

# 해설
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])
'''

'''
대표값

N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세 요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.
▣
10 45
▣
74
입력예제 1
73 66 87 92 67 75 79 75 80
출력예제 1 7


# 나의 풀이
n = int(input())
a = list(map(int, input().split()))

toal = sum(a)

p_min = 0
p_max = 0

# 해설
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min=2417000000

for idx, x in enumerate(a):
    tmp=abs(x-ave) # 평균 차이 절대값
    if tmp<min: # 만약 절대값이 기존 최소값보다 작으면
        min=tmp # 최소값을 바꿔준다
        score=x # 절대값이 같을 때를 위해 쓸 변수
        res=idx+1 # 몇 번째인지

    elif tmp==min: # 만약 절대값이 같을 때
        if x>score: # 현재 점수가 더 크다면(더 빠른 번호를 찾기 때문에 그 후 값은 필요없음)
            score=x # 점수를 바꿔줌
            res=idx+1
'''

'''
정다면체

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.
▣ 입력예제 1 46
▣ 출력예제 1 567
'''
# 나의 풀이
from collections import Counter
 
n, m = map(int, input().split())
arr = []

for i in range(1, n+1):
    for k in range(1, m+1):
        arr.append(i+k)

counter = Counter(arr)
print(dict(counter))

cnt = 0
result = []
for k, v in counter.items():
    if cnt < v:
        cnt = v
        
for k, v in counter.items():
    if cnt == v:
        result.append(k)
print(cnt)
print(result)

# 해설
n, m = map(int, input().split())
cnt = [0]*(n+m+3) # 배열을 +3으로 넉넉하게 잡음
max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end = ' ')