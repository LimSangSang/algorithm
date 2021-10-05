'''
2021.10.04
[이것이 코딩테스트다] p.110 상하좌우

여행가 A는 N * N 크기의 정사각형 공간 위에 서있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
<입력예시 1> <출력 예시 1>
5           R R R U D D
'''
# 나의 답
n = map(int, input().split())

p=[1, 1]
data = list(map(str, input().split()))

print(len(data))
for i in range(len(data)):
    if data[i]== 'R':
        np=p[1]+1
        if 0<np<6: 
            p=[p[0], p[1]+1]
            print('---R---')
            print(p)
        
    elif data[i]== 'L':
        np=p[1]-1
        if 0<np<6: 
            p=[p[0], p[1]-1]
            print('---P---')
            print(p)
        
    elif data[i]== 'U':
        np=p[0]-1
        if 0<np<6: 
            p=[p[0]-1, p[1]]
            print('---U---')
            print(p)
        
    elif data[i]== 'D':
        np=p[0]+1
        if 0<np<6: 
            p=[p[0]+1, p[1]]
            print('---D---')
            print(p)
        
print(p)

# 해설
'''
이 문제를 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하게 된다. 예를 들어 이동 횟수가 N번인 경우 시간 복잡도는 O(N)이다. 따라서 이 문제의 시간 복잡도는 매우 넉넉한 편이다.
'''
n = map(int, input().split())
x, y = 1, 1
plans = input().splist()

# L, R, U, D에 따른 이동 방향
dx= [0, 0, -1, 1]
dy= [-1, 1, 0, 0]
move_types=['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

'''
2021.10.04
[이것이 코딩테스트다] p.113 시각

정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
<입력예시 1> <출력 예시 1>
5           11475
'''
# 나의 답(오답)
# 첫 번째 조건부터 잘못되었다. 
n = str(input())

count=0
for i in range(int(n)+1):
    if '3' in str(i):
        count+=1
    else:
        for k in range(60):
            if '3' in str(k):
                count+=1
                
            else:
                for m in range(60):
                    if '3' in str(m):
                        count+=1
                        
print(count)

# 해답
h = int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)

'''
2021.10.05
[이것이 코딩테스트다] p.115 왕실의 나이트

8 * 8 좌표 평면이 있다. 나이트는 말을 타고 있기에 이동할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이때 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.
<입력예시 1> <출력 예시 1>
a1         2
<입력예시 2> <출력 예시 2>
c2         6
'''

# 나의 답
data = str(input())
move=['R', 'L', 'U', 'D']
a=['a','b','c','d','e','f','g','h']
print(type(int(data[1])) ,type(a.index(data[0])+1))
now=[int(data[1]) ,a.index(data[0])+1]
p=now
count=0
for i in move:
    if i=='R':
        if p[0]+1>0 and p[1]+2>0: 
            p=[p[0]+1, p[1]+2]
            p=now
            count+=1 
            print('R 1', p[0]+1, p[1]+2)
        if p[0]-1>0 and p[1]+2>0: 
            p=[p[0]-1, p[1]+2]
            p=now
            count+=1 
            print('R 2', p[0]-1, p[1]+2)
            
    if i=='L':
        if p[0]+1>0 and p[1]-2>0: 
            p=[p[0]+1, p[1]-2]
            p=now
            count+=1 
            print('L 1', p[0]+1, p[1]-2)
        if p[0]-1>0 and p[1]-2>0: 
            p=[p[0]-1, p[1]-2]
            p=now
            count+=1 
            print('L 2', p[0]-1, p[1]-2)
            
    if i=='U':
        if p[0]+2>0 and p[1]-1>0: 
            p=[p[0]+2, p[1]-1]
            p=now
            count+=1 
            print('U 1', p[0]+2, p[1]-1)
        if p[0]+2>0 and p[1]+1>0: 
            p=[p[0]+2, p[1]+1 ]
            p=now
            count+=1 
            print('U 2', p[0]+2, p[1]+1)
            
    if i=='D':
        if p[0]-2>0 and p[1]-1>0: 
            p=[p[0]-2, p[1]-1]
            p=now
            count+=1 
            print('D 1', p[0]-2, p[1]-1)
        if p[0]-2>0 and p[1]+1>0: 
            p=[p[0]-2, p[1]+1 ]
            p=now
            count+=1 
            print('D 2', p[0]-2, p[1]+1)
        
print(count)

# 해답
'''
나이트의 이동 경로를 steps 변수에 넣는다면, 이 2가지 규칙에 따라 steps=[(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]로 값을 대입할 수 있다. 

이제 나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음, 8 * 8 좌표 평면에 있는지 확인하면 된다. 이 과정은 반복문으로 처리할 수 있다.
'''

input_data=input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result=0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result+=1
print(result)