# 문제1. 그래프와 인접행렬
'''
name = 'ABED'
# 인접행렬 하드코딩
MAP = [[1, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 1, 0, 0],
       [1, 1, 0, 0]]
n = int(input())
# 노드의 개수
for i in range(4):
    if MAP[n][i] == 0: continue
    # 인접행렬이 0이면 반복문 처음으로 돌아간다
    print(name[i])
'''

# 문제2. 인접행렬 만들고 연결된 노드 출력
'''
name = 'ABCDE'
MAP = [[0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0]]
ch = input()
# 아스키코드 만드는 내장함수
n = ord(ch) - ord('A')

for i in range(5):
    if MAP[n][i] == 0: continue
    print(chr(i+ord('A')))
'''

# 문제3. 빈 배열을 만들고 append만 사용해서 [[3,5],[]] 출력
'''
m = []
m.append([])
m.append([3,5])
print(m)
'''

# 문제4. 배열 만들고 원소 넣기
'''
arr = [[] for _ in range(4)]
arr[0].append(4)
arr[0].append(2)
arr[0].append(5)
arr[0].append(1)
arr[0].append(1)

arr[1].append(3)
arr[1].append(4)
arr[1].append(1)

arr[3].append(1)
arr[3].append(1)
arr[3].append(2)
arr[3].append(3)

for lst in arr:
    print(*lst)
'''

# 문제5. 모든 원소를 출력하고싶다
'''
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end='')
    print()
'''

# 문제6. 역순으로 리스트 뒤집기
'''
arr1 = ['A','B','T']
arr2 = []
arr3 = ['R','S']

print(*arr1[::-1])
print(arr2)
print(*arr3[::-1])
'''
'''
m = [[] for _ in range(3)]
m[0] = ['A','B','T']
m[2] = ['R','S']

for y in range(len(m)):
    for x in range(len(m[y])-1,-1,-1): #0까지 1씩 감소
        print(m[y][x],end='')
    print()
'''

# 인접리스트 vs 인접행렬
# 인접리스트가 메모리를 더 적게 쓴다
# 입력데이터에 따라 사용하는게 다르다
'''
alist = list([] for _ in range(4)) # 4 노드의 개수

alist[1] = [0,3]
alist[2] = [1,3]
print(alist)
'''

# 문제7. 인접리스트를 하드코딩하고, n을 입력받을때 name을 출력
'''
alist = list([]for _ in range(5))
n = int(input())
name = 'DUSRK'
alist[0]=[1,3,4]
alist[1]=[2,3]
alist[3]=[2,4]
alist[4]=[1,3]

# for i in alist[n]:
#     print(name[i])
for i in range(len(alist[n])):
    print(name[alist[n][i]])
'''

#  문제8. 인접행렬 하드코딩 및 특정 번호를 입력하면 자식노드 이름 출력
'''
name = 'ABTQVX'
MAP = [[0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

n = int(input())

for i in range(6):
    if MAP[n][i] == 0:
        continue
    print(name[i])
'''

# 문제9. DFS 인접행렬 , 탐색 순서를 출력하세요
'''
MAP = [[0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

def dfs(now):
    print(now,end=' ')
    for i in range(6):
        if MAP[now][i] == 0:
            continue
        dfs(i)
dfs(0)
'''

# 문제10. DFS 인접 리스트 ( 노드 값을 출력 )
'''
name = 'ABTQVX'
def dfs(now):
    print(name[now],end=' ')
    for i in range(len(m[now])):
        next = m[now][i]
        dfs(next)

m = [ [] for _ in range(6) ]
m[0] = [1, 2, 3]
m[1] = [4, 5]
dfs(0)
'''

# 문제11. path배열 추가 ( 흔적기록 )
'''
path = [0] * 10

def dfs(level,now):
    global path
    print(chr(ord('A')+now),end=' ')
    for i in range(len(m[now])):
        next = m[now][i]
        # 'A'에서 'B'로 들어간다
        path[level+1] = chr(ord('A')+next)
        dfs(level+1,next)
        # 갔다가 돌아오면 지워준다
        path[level+1] = 0


m = [[] for _ in range(6)]
m[0] = [1, 2]
m[1] = [3]
m[2] = [4, 5]
dfs(0,0)

'''

# 문제12. 이진트리의 DFS
# 문제 12-1. path 배열 추가
'''
bt = ['0', 'A', 'B', 'T', 'R', 'S', 'V']
bt += [0]*100
path = [0]*100
def dfs(level,now):
    # 왼쪽 8 잘못탐색 return
    # 오른쪽이면 9 잘못 탐색 return
    # 최대 13 잘못 탐색 return
    if bt[now] == 0: return
    print(bt[now])
    # 왼쪽 자식
    path[level+1] = bt[now*2]
    dfs(level+1,now*2)
    # path[level+1] = 0
    # 오른쪽 자식
    path[level+1] = bt[now*2+1]
    dfs(level+1,now*2+1)
    # path[level+1] = 0
# 이진트리의 시작노드는 1부터
dfs(1,1)
'''

# 문제13. 인접리스트, 그래프의 dfs 탐색
'''
arr = [[] for _ in range(4)]
arr[0] = [1, 3]
arr[1] = [2]
arr[2] = [0, 3]
arr[3] = [2]
used = [0] * 4


def dfs(now):
    print(now, end=' ')
    for i in range(len(arr[now])):
        next = arr[now][i]
        if used[next] == 1:
            continue
        # 방문했던곳을 기록
        used[next] = 1
        # 한번도 안간 곳이라면 재귀호출
        dfs(next)


used[0] = 1
dfs(0)
'''

# 문제14. 인접행렬, 그래프 dfs탐색, used배열 지우지 않기 - 모든 노드 1회씩 탐색
'''
def dfs(now):
    print(now, end=' ')
    for i in range(4):
        # 길이 없으면 무시
        if used[i] == 0:
            if arr[now][i] == 1:
                used[i] = 1
                dfs(i)


arr = [[0, 1, 0, 1],
       [0, 0, 1, 0],
       [1, 0, 0, 1],
       [0, 0, 1, 0]]
used = [0] * 4

used[0] = 1
dfs(0)
'''

# 문제 15. 인접 행렬 그래프 DFS, Used 배열 지우기 ---> 모든 경로 1회 탐색
'''
# 인접행렬 초기화
MAP = [[0, 1, 1],
       [0, 0, 1],
       [1, 0, 0]]
# used 배열 초기화
used = [0] * 3
cnt = 0 # 경로 갯수 초기화
# 시작 노드 방문 기록
used[0] = 1

def dfs(now):
    global cnt 
    # end노드 2번노드
    if now == 2:
        cnt += 1
        return

    for i in range(3):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue # 이미 방문 했으면 안가겠음
        used[i] = 1 # 갔다고 기록한다
        dfs(i)
        used[i] = 0 # 지움. 다음에 또 가기 위해서

# start는 0번 노드
dfs(0)
print(cnt)
'''

# 가중치 값 : 비용 문제
# 문제16. 0에서 2로 이동하는데 경로마다 각각 비용이 얼마나 드나요
# used 배열 지우기, 가중치 인접행렬, 매개변수 sum_v 추가
'''
MAP = [[0,7,20,8],
       [0,0,5,0],
       [15,0,0,0],
       [0,0,6,0]]
used = [0]*4

def dfs(now,sum_v):
    if now == 2:
        print(sum_v,end=' ')

    for i in range(4):
        if MAP[now][i] == 0:
            continue
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(i,sum_v+MAP[now][i])
        used[i] = 0

used[0] = 1
dfs(0,0)
'''
# 문제17-1.모든 노드 1회 탐색 ( used 초기화 안시키기 )
'''
def dfs(now):
    print(now,end=' ')
    for i in range(len(arr[now])):
        n = arr[now][i]
        if used[n] == 1:
            continue
        used[n] = 1
        dfs(n)


arr = [[] for _ in range(6)]
arr[0] = [1, 2, 3]
arr[1] = [0, 2, 3]
arr[2] = [0, 1]
arr[3] = [0, 1, 2]
arr[4] = [2, 5]
used = [0] * 6
dfs(4)
'''

# 모든 경로 1회 탐색 ( used배열 계속 초기화 시키기 )
'''
def dfs(now):
    print(now,end=' ')
    for i in range(len(arr[now])):
        n = arr[now][i]
        if used[n] == 1:
            continue
        used[n] = 1
        dfs(n)
        used[n] = 0


arr = [[] for _ in range(6)]
arr[0] = [1, 2, 3]
arr[1] = [0, 2, 3]
arr[2] = [0, 1]
arr[3] = [0, 1, 2]
arr[4] = [2, 5]
used = [0] * 6
dfs(4)
'''
# ========================================================
# 강사님 코드
MAP = [[0, 2, 6, 3, 0, 0],
       [2, 0, 7, 4, 0, 0],
       [6, 7, 0, 0, 0, 0],
       [3, 4, 2, 0, 0, 0],
       [0, 0, 1, 0, 0, 7],
       [0, 0, 0, 0, 0, 0]]
cnt = 0
min_v = float('inf')
max_v = float('-inf')

def dfs1(now):
    print(now, end=' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs1(i)


# =================================================

def dfs2(now):
    print(now, end=' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs2(i)
        used[i] = 0


# ====================================================================

used = [0] * 6
dfs1(4)
print()
used = [0] * 6
dfs2(4)


def dfs3(now):
    global cnt
    # b에 도착
    if now == b:
        cnt += 1
        return

    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs3(i)
        used[i] = 0


def dfs4(now, sum_v):
    global cnt
    global min_v
    global max_v

    if now == b:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)

    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs4(i,sum_v+MAP[now][i])
        used[i] = 0

a,b = map(int,input().split())
used = [0] * 6
used[a] = 1
dfs4(a,0)
print(cnt)
print(max_v)
print(min_v)