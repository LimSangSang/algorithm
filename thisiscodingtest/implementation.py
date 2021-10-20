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


'''
2021.10.06
[이것이 코딩테스트다] p.118 게임 개발

캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.

맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸의 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

입력 조건
1. 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분되어 입력한다.(3 <= N,M <= 50)
2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 다음과 같이 4가지가 존재한다.
   0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
3. 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.  맵의 외곽은 항상 바다로 되어있다.
   0: 육지, 1: 바다
4. 처음에 캐릭터가 위치한 칸의 상태는 항상 육지이다. 

<입력 예시>
4 4      # 4 * 4 맵의 생성
1 1 0    # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1  # 첫 줄은 모두 바다
1 0 0 1  # 둘째 줄은 바다/육지/육지/바다
1 1 0 1  # 세째 줄은 바다/바다/육지/바다
1 1 1 1  # 넷째 줄은 모두 바다
'''

# 나의 풀이
# 풀지 못함

# 해설
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문처리
d[x][y] = 1 

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

