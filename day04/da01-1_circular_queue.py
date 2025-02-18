# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    return queue[(front + 1) % SIZE]

# 전역 변수 선언
SIZE = int(input('큐 크기 입력 > '))
queue = [None] * SIZE
front = rear = 0

# 메인 코드
if __name__ == '__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) > ').upper()
        
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태: {queue}')
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터: {data}')
            print(f'큐 상태: {queue}')
            if isQueueEmpty():
                front = rear = -1
        elif select == 'V':
            data = peek()
            print(f'확인 데이터: {data}')
            print(f'큐 상태: {queue}')
        else:
            print('')