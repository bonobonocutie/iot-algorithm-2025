# 단순 연결리스트

## 전역 변수
memory = [] # 컴퓨터 메모리처럼 보이게 만든 변수
head, prev, curr = None, None, None # 항상 첫번째 노드, curr 바로 앞의 노드, 현재 선택한 노드
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 연결리스트를 만들 데이터

class Node:#
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link

    def getData(self):
        return self.__data
    
    def getLink(self):
        return self.__link
    
    def __str__(self):
        return self.__data
    
def printNodes(start):
    curr = start
    
    if curr == None: return
    
    print(curr.getData(), end=' -> ')

    while curr.getLink() != None: # 현재링크의 다음링크가 있는 동안
        curr = curr.getLink() # 다음 노드를 가리킴
        if curr.getLink() == None: # 더이상 다음 노드가 없으니 화살표 필요없음
            print(curr.getData())
        else:
            print(curr.getData(), end=' -> ')

    print()

def insertNode(findData, insertData):
    global memory, head, prev, curr # 전역변수를 가져와서 insertNode함수 안에서 쓰겠다는 선언

    # 맨 처음에 데이터 삽입
    if head.getData() == findData:
        node = Node(insertData)
        node.setLink(head) # 현재 head가 가리키는 node를 새노드의 링크로 연결
        head = node # head는 새 node로 설정
        return # 더이상 밑으로 실행안되도록 함수

    # 중간에 데이터 삽입
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr.getData() == findData:
            node = Node(insertData)
            node.setLink(curr)
            prev.setLink(node)

            return

    # 마지막에 데이터 삽입
    node = Node(insertData)
    curr.setLink(node)

def deleteNode(deleteData):
    global memory, head, prev, curr

    if head.getData() == deleteData: # 첫번째 노드 삭제
        curr = head
        head = head.getLink()
        del(curr)
        return
    
    curr = head # 중간 노드 삭제
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr is None: return # 단순로직으로 예외처리
        if curr.getData() == deleteData:
            prev.setLink(curr.getLink()) # 지울 노드의 링크를 prev에서 가리키도록
            del(curr)

def findNode(findData):
    global prev, curr, head, memory

    curr = head
    if curr.getData() == findData:
        return curr
    
    while curr.getLink() != None:
        curr = curr.getLink()
        if curr.getData() == findData:
            return curr

    return None # 찾는 데이터가 없음

# 연결리스트 생성 구현
if __name__ == '__main__':
    node = Node(dataArray[0])
    head = node
    memory.append(node)

    for name in dataArray[1:]: # '정연'부터 사용
        prev = node # 다현이 들어있는 노드를 prev 할당
        node = Node(name) # 0/정연, 1/쯔위, 2/사나, 3/지효
        prev.setLink(node) # 이전노드에 현재노드를 연결
        memory.append(node)

    printNodes(head)

    # 5개 데이터를 가지는 연결리스트 생성 끝

    # 데이터 삽입 구현
    insertNode('다현', '화사')
    printNodes(head)

    insertNode('사나', '솔라')
    printNodes(head)

    insertNode('', '문별')
    printNodes(head)

    # 데이터 삭제
    deleteNode('화사')
    printNodes(head)
    
    # 데이터 검색
    fNode = findNode('화사')
    print(fNode)

    fNode = findNode('다현')
    print(fNode)