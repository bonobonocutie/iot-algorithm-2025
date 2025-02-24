# 이미지 처리

from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('이미지 처리')

photo = PhotoImage(file='../iot-python-2025/image/cupdog.png')

photoAry = []
h = photo.height() # 600
w = photo.width() # 600
for i in range(h): # 행렬 row와 동일
    for k in range(w): # 행열 col과 동일
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3 # 평균치
        photoAry.append(value)

print(len(photoAry)) # 360000 리스트가 생성

# 색상들을 정리. 127보다 작으면 검은색, 127보다 크면 흰색
for i in range(len(photoAry)):
    if photoAry[i] <= 127:
        photoAry[i] = 0 # black
    else:
        photoAry[i] = 255 # white

# 흑백이미지로 변경
pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        # photo에 각 위치의 색상을 pthotoAry에 들어있는 값으로 변경
        photo.put(f'#{r:02x}{g:02x}{b:02x}', (i, k)) 

paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)

root.mainloop()