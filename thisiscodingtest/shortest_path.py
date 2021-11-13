'''
[이것이 코딩테스트다] p.259 미래도시
A는 많은 도시가 모여 있는 공중 미래 도시에 있다. 공중 미래 도시는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 도로를 통해 연결되어 있다.
A는 현재 1번 회사에 있고, X번 회사에 방문해야 한다. 특정 회사에 도착하려면 연결되어 있는 도로를 이용해야하고 2개의 회사는 양방향으로 이동할 수 있다.
특정 회사가 다른 회사로 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다. 
A는 1번 회사에서 출발해 K번 회사를 방문한 뒤 X번 회사로 가는게 목표다. 이때 최대한 빠르게 이동하려고 한다.
'''
# 나의 답(못 품)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def get_smallest_node():
    min_value=INF
    index = 0
    
# 해설 
'''
전형적인 프로이드 워셜 알고리즘이다. 1번 노드에서 X를 거쳐 K로 가는 최단 거리라는게 핵심이다.
'''
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1를 출력
if distance >= INF:
    print('-1')
else:
    print(distance)


'''
2021.11.13
[이것이 코딩테스트다] p.262 전보
어떤 나라에서는 N개의 도시가 있다. X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, X에서 Y로 향하는 통로가 설치되어 있어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메세지를 보낼 수 없다. 또한 통로를 거쳐 메세지를 보낼 때는 일정 시간 소요된다.
도시 C에서 보낸 메세지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메세지를 받는 데까지 걸리는 시간을 얼마인가.

입력조건
1. 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메세지를 보내고자 하는 도시 C가 주어진다.
2. 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메세지가 전달되는 시간이 Z라는 의미이다.
'''
# 해설
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1를 출력
print(count -1, max_distance)
        