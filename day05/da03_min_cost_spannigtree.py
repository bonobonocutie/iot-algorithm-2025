# 최소 비용 신장 트리
from operator import itemgetter

# 전역변수
SIZE = 6
GROAD = None
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

# 클래스 선언
class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 개선된 그래프 출력
def printGraph(g):
    global nameAry
    print('\t', end='')
    for v in range(g.size):
        print(nameAry[v], end='\t')
    print()

    for row in range(g.size):
        print(nameAry[row], end='\t')
        for col in range(g.size):
            print(f'{g.graph[row][col]:>4d}', end='\t')
        print()
    print()

# 특정정점에 그래프가 연결되었는지 확인하는 함수
def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0 # A
    stack.append(current) # Stack push(A)
    visitedAry.append(current) # 방문기록 A

    while len(stack) != 0 : # Stack 길이가 0이 되면 모든 정점을 방문했다는 뜻
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0: # 간선이 있다
                if vertex in visitedAry: # 도착점이 이미 방문했으면 
                    continue
                else:
                    next = vertex # 다음번 방문할 정점
                    break

        if next != None: # 다음 방문할 정점이 있으면
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

# 초기화
G = Graph(SIZE)

G.graph[춘천][서울] = 10; G.graph[춘천][속초] = 15
G.graph[서울][춘천] = 10; G.graph[서울][속초] = 40 ; G.graph[서울][대전] = 11; G.graph[서울][광주] = 50
G.graph[속초][춘천] = 15; G.graph[속초][서울] = 40; G.graph[속초][대전] = 12
G.graph[대전][서울] = 11; G.graph[대전][속초] = 12 ; G.graph[대전][부산] = 30; G.graph[대전][광주] = 20
G.graph[광주][서울] = 50; G.graph[광주][대전] = 20; G.graph[광주][부산] = 25
G.graph[부산][대전] = 30; G.graph[부산][광주] = 25

print('## 자전거 도로 전체 연결도 ##')
printGraph(G)

# 가중치 간선 목록
edgeAry = []
for row in range(SIZE):
    for col in range(SIZE):
        if G.graph[row][col] != 0: # 가중치가 있음
            edgeAry.append((G.graph[row][col], row, col))

print('## 간선목록 -> ', end=' ')
print(edgeAry)

# 가중치별 간선 내림차순 정렬
# itemgetter(0) -> (weight, slot, elot) 중 weight로 정렬하겠다
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True)
print('## 간선목록 정렬 -> ', end=' ')
print(edgeAry)

# 중복간선 제거
newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

print('## 중복간선 제거 목록 -> ', end=' ')
print(newAry)

# 가중치 높은 간선부터 제거
index = 0
# 0:춘천, 1:서울, 2: 속초, 3:대전, 4:광주, 5:부산
while len(newAry) > (SIZE - 1): # 간선의 수가 (정점수 - 1) 될때까지 반복
    start = newAry[index][1] # 서울부터 시작
    end = newAry[index][2] # 광주부터 시작
    saveWeight = newAry[index][0] # 현재 가중치 저장(복원ㅇ르 위해서)
    
    G.graph[start][end] = 0 # 무조건 지움
    G.graph[end][start] = 0 # 무방향이라 양쪽으로 값이 다 있음

    startYN = findVertex(G, start) # 서울에 연결된 간선 확인
    endYN = findVertex(G, end) # 광주에 연결된 간선 확인

    if startYN and endYN: # 둘 다 다른 간선 있으니까 지금 간선을 지워도 됨
        del(newAry[index])
    else: # 연결된 간선이 없으니까 지웠던 인접행렬 값을 원상복귀
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1

# 결과 출력
print('## 최소비용 신장트리 결과 ##')
printGraph(G)
