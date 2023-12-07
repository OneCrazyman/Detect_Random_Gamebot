import pyautogui as pag
import random, time
import keyboard
import threading, os
import pygetwindow as gw
import pywinauto
import numpy as np

#변수
process = 2
base_std_dev = 60

#딕셔너리
dic_key = {
    "esc":100,
    "enter":313,
    "alt":602,
    "f4":104,
    "f9":109,
    "f10":110,
    "f11":111,
    "f12":112,
    "0":210,
    "1":201,
    "2":202,
    "3":203,
    "4":204,
    "5":205,
}

####Class
#항상 작동중인 스레드
class always(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self) :
        while 1:
            if keyboard.is_pressed('F11'or'F12'):
                kill()


####Method
#터치영역 설정(메이플M)
def setTouchRegion_m():
    #가방
    TouchBox[0] = [
        region_game[0] + 1150,
        region_game[1] + 50,
        40,
        40,
    ]
    #자동사냥
    TouchBox[1] = [
        region_game[0] + 400,
        region_game[1] + 660,
        57,
        57,
    ]
    #일일과제 탭
    TouchBox[2] = [
        region_game[0] + 1030,
        region_game[1] + 50,
        40,
        40,
    ]
    #일일과제 받기버튼
    TouchBox[3] = [
        region_game[0] + 1117,
        region_game[1] + 163,
        130,
        50,
    ]
    #이벤트창 끄기
    TouchBox[4] = [
        region_game[0] + 1010,
        region_game[1] + 151,
        17,
        22,
    ]
    #게임 로비 중앙 박스 width/2 height/2
    TouchBox[5] = [
        region_game[0] + region_game[2]/4,
        region_game[1] + region_game[3]/4,
        region_game[2]/2,
        region_game[3]/2,
    ]
    #인벤토리 판매 버튼2
    TouchBox[6] = [
        region_game[0] + 1080,
        region_game[1] + 689,
        182,
        42,
    ]
    #거래소
    TouchBox[7] = [
        region_game[0] + 973,
        region_game[1] + 50,
        40,
        40,
    ]
    #빠른 컨텐츠 이용
    TouchBox[8] = [
        region_game[0] + 910,
        region_game[1] + 50,
        40,
        40,
    ]
    #hp포션 단축키
    TouchBox[9] = [
        region_game[0] + 1211,
        region_game[1] + 350,
        62,62,
    ]
    #적정 스타포스 필드 첫번째
    TouchBox[10] = [
        region_game[0] + 680,
        region_game[1] + 230,
        548,59,
    ]

# pywinauto 권한 설정 필요
# 관리자 cmd에서 py인터럽트 실행으로 권한부여
def bring_to_window(title) :
    try:
        print("창가져오기..")
        win = gw.getWindowsWithTitle(title)[0] 
        if win.isActive == False:
            pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
        win.activate() #윈도우 활성화
        return 1
    except IndexError:
        return 0

#버튼클릭 (locateCenterOnScreen)
def click_btn(pos_img,width,height,**kwargs):
    duration = float(kwargs.get("duration", randInterval()))
    widthHalf = width/2
    heightHalf = height/2
    btn_pos = {
        'top_left':{
            'x': pos_img.x-widthHalf,
            'y': pos_img.y-heightHalf,
        },
        'bottom_right':{
            'x': pos_img.x+widthHalf,
            'y': pos_img.y+heightHalf,
        }
    }
    pag.moveTo(
        x = random.uniform(btn_pos['top_left']['x'], btn_pos['bottom_right']['x']),
        y = random.uniform(btn_pos['top_left']['y'], btn_pos['bottom_right']['y']),
        duration = duration
    )
    pag.mouseDown()
    time.sleep(random.uniform(0.1234,0.1223))
    pag.mouseUp()
    time.sleep(random.uniform(0.1544,0.3222))

#버튼클릭2(locateOnScreen)
def click_btnTwo(pos_img,**kwargs):
    duration = float(kwargs.get("duration", random.uniform(0.022,0.056)))
    pag.moveTo(
        x = random.uniform(pos_img[0], pos_img[0] + pos_img[2]),
        y = random.uniform(pos_img[1], pos_img[1] + pos_img[3]),
        duration = duration
    )
    pag.mouseDown()
    time.sleep(random.uniform(0.1234,0.1223))
    pag.mouseUp()
    time.sleep(random.uniform(0.1544,0.3222))

#단순클릭
def push_btn(typing):
    time.sleep(random.uniform(0.0320,0.0456))
    pag.keyDown(typing)
    time.sleep(random.uniform(0.256,0.356))
    pag.keyUp(typing)

#프로그램 종료
def kill(**kwargs):
    global process
    process = int(kwargs.get("process", process))
    print("서브스레드,메인스레드 종료")
    pid = os.getpid()
    os.kill(pid, process)

#std_dev 계산
def calculate_std_dev(width, height):
    ratio = width / height if width < height else height / width
    std_dev = 10 ## 임시
    return std_dev,ratio

#classDD 우측 마우스클릭
def dd_rightclick(pos_img,dd_dll,**kwargs):
    interval = float(kwargs.get("interval", randInterval()))

    #
    left = pos_img[0]
    top = pos_img[1]
    width = pos_img[2]
    height = pos_img[3]

    # 정규 분포의 평균과 표준 편차 설정
    mean_x = 0
    mean_y = 0

    std_dev,ratio = calculate_std_dev(width,height)
    std_dev = float(kwargs.get("std_dev", std_dev))

    # 범위 설정
    x_range = (-width/2, width/2)
    y_range = (-height/2, height/2)
    
    x = np.random.normal(mean_x, std_dev)
    y = np.random.normal(mean_y, std_dev)
    
    #x,y배율 조정
    if width > height: x /= ratio
    else: y /=ratio
    
    # 점이 범위를 벗어나지 않도록 조정
    while x < x_range[0] or x > x_range[1] or y < y_range[0] or y > y_range[1]:
        x = np.random.normal(mean_x, std_dev)
        y = np.random.normal(mean_y, std_dev)
    
    ## 대칭이동
    x = int(x + left + width/2)
    y = int(y + top + height/2)

    dd_dll.DD_mov(x,y)
    time.sleep(interval*2)
    dd_dll.DD_btn(4)
    time.sleep(interval)
    dd_dll.DD_btn(8)
    time.sleep(interval)

    return x,y

#classDD 단순 마우스클릭
def dd_click_only(dd_dll,**kwargs):
    interval = float(kwargs.get("interval", randInterval()))
    double = int(kwargs.get("double", 0))

    dd_dll.DD_btn(1)
    time.sleep(interval)
    dd_dll.DD_btn(2)
    time.sleep(interval)
    if (double):
        dd_dll.DD_btn(1)
        time.sleep(interval)
        dd_dll.DD_btn(2)
        time.sleep(interval)

#classDD 마우스클릭(locateOnScreen)
def dd_click(pos_img,dd_dll,**kwargs):
    
    double = int(kwargs.get("double", 0))
    interval = float(kwargs.get("interval", randInterval()))
    #
    left = pos_img[0]
    top = pos_img[1]
    width = pos_img[2]
    height = pos_img[3]

    # 정규 분포의 평균과 표준 편차 설정
    mean_x = 0
    mean_y = 0

    std_dev,ratio = calculate_std_dev(width,height)
    std_dev = float(kwargs.get("std_dev", std_dev))

    # 범위 설정
    x_range = (-width/2, width/2)
    y_range = (-height/2, height/2)
   
    x = np.random.normal(mean_x, std_dev)
    y = np.random.normal(mean_y, std_dev)
    
    #x,y배율 조정
    if width > height: x /= ratio
    else: y /=ratio

    # 점이 범위를 벗어나지 않도록 조정
    while x < x_range[0] or x > x_range[1] or y < y_range[0] or y > y_range[1]:
        x = np.random.normal(mean_x, std_dev)
        y = np.random.normal(mean_y, std_dev)
    
    ## 대칭이동
    x = int(x + left + width/2)
    y = int(y + top + height/2)
    
    #append 대신 마우스클릭 사용
    dd_dll.DD_mov(x,y)
    time.sleep(interval*2)
    dd_dll.DD_btn(1)
    time.sleep(interval)
    dd_dll.DD_btn(2)
    time.sleep(interval)
    if (double):
        dd_dll.DD_btn(1)
        time.sleep(interval)
        dd_dll.DD_btn(2)
        time.sleep(interval)

    return x,y


#classDD 키입력
def dd_key(key,dd_dll):
    key = dic_key[key]
    dd_dll.DD_key(key,1)
    time.sleep(randInterval())
    dd_dll.DD_key(key,2)
    time.sleep(randInterval())

#delay값
def randInterval():
    return random.uniform(0.0855,0.0232)
def randShort():
    return random.uniform(0.5111,0.3233)
def randMiddle():
    return random.uniform(1.1122,0.3333)
def randLong():
    return random.uniform(3.1111,0.5233)

def whatColorTitlebar(color):
    if color == "white": name = "iconWhite.png" 
    elif color == "black": name = "iconBlack.png"
    return name