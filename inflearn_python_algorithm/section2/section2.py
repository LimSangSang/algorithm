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
'''

'''
자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.
▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.
▣ 입력예제 1 3
125 15232 97
▣ 출력예제 1 97

# 나의 풀이
n = input()
num=0
total=0

arr = list(map(str, input().split()))
for i in range(int(n)):
    print(arr[i])
    
    temp_total = sum([int(k) for k in arr[i]])
    print(temp_total)

    if temp_total > total:
        total = temp_total
        num=arr[i]

print(num)
    
# 해설
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum += x % 10
        x = x // 10
    return sum
max = -2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)
'''

'''
소수(에라토스테네스 체)

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.
▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.
▣ 입력예제 1 20
▣ 출력예제 1 8

# 내 풀이(틀림)
n = int(input())
arr = []
for i in range(2, n+1):
    if i // i == 0:
        arr.append(i)
        print(i)

print(arr)

# 해설
n=int(input())
ch=[0]*(n+1)
cnt=0
print(ch)
for i in range(2, n+1):
    print('>', i, ch[i])
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1

print(cnt)
'''

'''
뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.
▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 100,000를 넘지 않는다.
▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
▣ 입력예제 1
5
32 55 62 3700 250
▣ 출력예제 1 23 73


import math

# 나의 풀이
n = int(input())
a = list(map(int, input().split()))
result = []

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if x % i == 0:
            return False
    print(x, end=' ')
    result.append(x)
    return True

def reverse(x):
    return int(str(x)[::-1])
for i in a:
    item = reverse(i)
    is_prime_num(item)
    
print('결과')
print(result)


# 해설
n = int(input())
a = list(map(int, input().split()))
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
'''

'''
주사위 게임

1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게 임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된 다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금 으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램 을 작성하시오
▣ 입력설명
첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람 들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
▣ 출력설명
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.
▣ 입력예제 1 3
336 222 625
▣ 출력예제 1 12000
'''
# 나의 답(못 품)
n = int(input())
result = []
for i in range(n):
    a, b, c =list(map(int, input().split()))
    max_score = max([a, b, c])    
    if (a == b == c):
        score = 10000+a*1000
        result.append(score)
    elif (a != b != c):
        score = max_score*100
        result.append(score)

# 해설
n = int(input())
res=0
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    
    if a==b and b==c:
        money=10000+a*1000
    elif a==b and a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money>res:
        res=money
print(res)
