# 문제1. 큐 예제 문제
'''
from collections import deque
q = deque()
q.append(5)
q.append(4)
q.append(3)

for i in range(5):
    num = q.popleft()
    q.append((num * 55 + 17) % 11)

while q:
    print(q[0])
    q.popleft()
'''
# 문제2. BFS리스트 , 인접리스트
'''
alist = [[]for _ in range(7)]

alist[5] = [3,1]
alist[3] = [2]
alist[1] = [4]
alist[4] = [0,6]

from collections import deque
q = deque()
q.append(5)

while q:
    now = q.popleft()
    print(now,end=' ')
    for i in range(len(alist[now])):
        next = alist[now][i]
        q.append(next)

'''
'''
from collections import deque
alist = [[] for _ in range(7)]
alist[0] = [1,2,3]
alist[2] = [4]
alist[3] = [5,6]
name = 'ACBQTPR'

q = deque()
# q에 시작값을 넣어줌으로써 시작
q.append(0)

while q:
    now = q.popleft()
    print(name[now],end = ' ')

    for i in range(len(alist[now])):
        next = alist[now][i]
        q.append(next)
'''
# 그래프 BFS 탐색
# 트리 <--> 그래프 : cycle이 있기때문에 무한 loop에 빠질 수 있다
# 문제3. 양방향 그래프, BFS 탐색, 인접리스트 , used배열
'''
from collections import deque

def bfs(now):
    q = deque()
    used = [0] * 5
    q.append(0)
    used[now] = 1

    while q:
        now = q.popleft()
        print(name[now],end=' ')
        for i in range(len(alist[now])):
            next = alist[now][i]
            if used[next] == 1:
                continue
            used[next] = 1
            q.append(next)

# 인접리스트 초기화
alist = [[] for _ in range(5)]
alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]
name = 'ABCDE'
# used배열

bfs(0)
'''
# BFS 마지막 문제 ♥
'''
from collections import deque

def bfs(start,end):
    q = deque()
    # used 배열
    used = [0] * len(alist)
    q.append((start,0))
    used[start] = 1

    while q:
        now, level = q.popleft()
        if now == end:
            return level

        for i in range(len(alist[now])):
            if alist[now][i] == 0: continue
            if used[i] == 1: continue
            used[i] = 1
            q.append((i,level+1))

    return -1


alist = [[]for _ in range(5)]
alist[0] = [1,4]
alist[1] = [3,4]
alist[2] = [0]
alist[3] = [4,0]

name = "ABCDE"
start = 0
end = 3

result = bfs(start,end)
print(result)

'''
# Union-Find
'''
boss = [0] * 10

def find(n):
    if boss[n] == 0:
        return n

    result = find(boss[n])
    return result

def Union(t1,t2):
    a = find(t1)
    b = find(t2)
    if a == b:
        return
    boss[b] = a

Union(6,7)
Union(5,6)
Union(1,2)

if find(2) == find(6) :
    print('같은그룹')
else:
    print('다른그룹')
'''

# Union_Find : 경로압축
'''
boss = [0] * 10


def find(n):
    if boss[n] == 0:
        return n

    result = find(boss[n])
    boss[n] = result #경로 압축 코드
    # boss[n] = find(boss[n])
    return boss[n]


def Union(t1, t2):
    a = find(t1)
    b = find(t2)
    if a == b:
        return
    boss[b] = a


Union(6, 7)
Union(5, 6)
Union(1, 2)

if find(2) == find(6):
    print('같은그룹')
else:
    print('다른그룹')
'''

# Union-Find 예제문제1
'''
같은 그룹이면 'O'
다른 그룹이면 'X'
'''
'''
boss = [0] * 10


def find(n):
    if boss[n] == 0:
        return n

    result = find(boss[n])
    boss[n] = result #경로 압축 코드
    # boss[n] = find(boss[n])
    return boss[n]


def Union(t1, t2):
    a = find(t1) # t1의 보스
    b = find(t2) # t2의 보스
    if a == b:
        return
    boss[b] = a


Union(1, 3)
Union(4, 2)
Union(9, 5)
Union(1, 4)

for x1,x2 in ((1, 5), (2, 9), (1, 4)):
    if find(x1) == find(x2):
        print('O')
    else:
        print('X')
'''
# Union-Find 예제문제2
# cycle이 있다 : 간선을 한번씩만 이용했을때 제자리로 돌아올 수 있다.
# cycle의 여부 : Union-Find로 알 수 있다 ( 양방향일때만 가능 )
'''
4
A B
B C
D E
C A
ㄴ> cycle 발견 ! 출력
[ 전략 ]
1. 문자를 아스키 코드로 바꾼다
2. a와 b가 같은 그룹이면 cycle 발견 ! 출력
'''
'''
boss = [0] * 200


def find(n):
    if boss[n] == 0:
        return n

    result = find(boss[n])
    boss[n] = result #경로 압축 코드
    # boss[n] = find(boss[n])
    return boss[n]


def Union(t1, t2):
    a = find(t1) # t1의 보스
    b = find(t2) # t2의 보스
    if a == b:
        return
    boss[b] = a


T = int(input())
for _ in range(T):
    a,b = map(ord,input().split())
    
    if find(a) == find(b):
        print('cycle발견!')
        break
    else:
        Union(a,b)
'''
'''
boss = [i for i in range(200)]

def find(n):
    if boss[n] == n:
        return n
    boss[n] = find(boss[n])  # 경로 압축
    return boss[n]

def Union(t1, t2):
    a = find(t1)
    b = find(t2)
    if a != b:
        boss[b] = a
        return True
    return False

N, T = map(int, input().split())  # N은 노드 수, T는 간선 수
lst = []
for _ in range(N):
    a, b, p = input().split()
    lst.append((ord(a) - ord('A'), ord(b) - ord('A'), int(p)))

lst.sort(key=lambda x: x[2])

sum_v = 0
for x1, x2, x3 in lst:
    if Union(x1, x2):
        sum_v += x3

print(sum_v)
'''
'''
def dfs(now,sum_v):
    global min_v

    if now == 5:
        min_v = min(min_v,sum_v)

    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1:continue
        used[i] = 1
        dfs(i,sum_v+MAP[now][i])
        used[i] = 0


arr = [[]for _ in range(6)]
MAP = [[0,15,0,30,0,0],
       [0,0,5,0,0,0],
       [0,0,0,6,2,0],
       [0,0,0,0,0,7],
       [0,0,0,0,0,1],
       [0,0,0,0,0,0]]

used = [0] * 6
min_v = float('inf')

used[0] = 1
dfs(0,0)
print(min_v)
'''
import heapq

MAP = [[0 for _ in range(6)] for _ in range(6)]

MAP[0][1] = 15
MAP[0][2] = 30
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[3][5] = 7
MAP[4][5] = 1

def dijkstra(start):
    n = len(MAP) # 노드수 6개
    result = [float('inf')] * n
    result[start] = 0 # 시작 노드 초기화
    # 우선순위 큐 초기화
    q = [(0, start)] # 비용, 노드

    while q:
        price, now = heapq.heappop(q) # 현재 최소 비용인 노드 선택

        if result[now] < price: continue # 이미 처리된 노드라면 continue

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] # 다음 노드까지의 비용
            price_sum = price + next_price
            if result[i] > price_sum : # 더 적은 비용 경로를 발견하면
                result[i] = price_sum # 최소 비용 업데이트
                heapq.heappush(q, (price_sum, i)) # 새로운 경로를 큐에 추가

    return result
# start 는 0
result = dijkstra(0)
print(f'노드 0부터 최소 비용 : {result}')
print(f'노드 0부터 5까지 최소 비용 : {result[5]}')