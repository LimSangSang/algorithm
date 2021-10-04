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
print(result)