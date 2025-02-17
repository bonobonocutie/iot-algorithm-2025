memory = []
head, prev, curr = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

class Node():
    def __init__(self, data):
        self.data = data
        self.link = None

def printNodes(start):
    curr = start
    if curr.link == None: return
    print(curr.data, end=' -> ')
    while curr.link != start:
        curr = curr.link
        if curr.link == start:  
            print(curr.data)
        else:
            print(curr.data, end=' -> ')

def insertNode(findData, insertData):
    global memory, head, prev, curr

    # 처음에 노드 삽입
    if head.data == findData:
        node = Node(insertData)    
        node.link = head
        last = head
        while last.link != head: # last가 head 되기 전 노드까지 이동
            last = last.link
        last.link = node # 마지막 전 노드의 다음 노드 = 추가한 노드
        head = node
        return # 추가한 노드의 다음이 head

    # 중간에 노드 삽입
    curr = head
    while curr.link != head:
        prev = curr
        curr = curr.link
        if curr.data == findData:
            node = Node(insertData)
            node.link = curr
            prev.link = node
            return
        
    # 마지막에 노드 삽입
    node = Node(insertData)
    curr.link = node
    node.link = head

def deleteNode(deleteData):
    global memory, head, prev, curr

    # 처음 노드 삭제
    if head.data == deleteData:
        curr = head
        head = head.link # 헤드 노드가 삭제되기 때문에 다음노드로 헤드 지정
        last = head
        while last.link != curr:
            last = last.link
        last.link = head
        del(curr)
        return

    #  처음 제외한 노드 삭제
    curr = head
    while curr.link != head:
        prev = curr
        curr = curr.link
        if curr.data == deleteData:
            prev.link = curr.link
            del(curr)
            return
        
def findNode(findData):
    global memory, head, prev, curr

    curr = head
    if curr.data == findData:
        return curr.data
    while curr.link != head:
        curr = curr.link
        if curr.data == findData:
            return curr.data
    return None

if __name__ == '__main__':
    node = Node(dataArray[0])
    head = node
    node.link = head # 자신이 자신과 연결된 형태
    memory.append(node)

    for data in dataArray[1:]:
        prev = node
        node = Node(data)
        prev.link = node
        node.link = head # 추가한 노드의 링크를 헤드와 연결
        memory.append(node)

    printNodes(head)

    # 데이터 삽입
    insertNode('다현', '화사')
    printNodes(head)

    insertNode('사나', '솔라')
    printNodes(head)
    
    insertNode('', '문별')
    printNodes(head)

    # 데이터 삭제
    deleteNode('다현')
    printNodes(head)
    
    deleteNode('쯔위')
    printNodes(head)

    deleteNode('화사')
    printNodes(head)

    # 데이터 검색
    fNode = findNode('화사')
    print(fNode)

    fNode = findNode('사나')
    print(fNode)

    fNode = findNode('지효')
    print(fNode)