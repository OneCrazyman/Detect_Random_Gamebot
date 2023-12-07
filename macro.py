import pyautogui as pag
import random, time
import pyperclip
import keyboard
import sys
sys.path.append('..')  # 상위 디렉토리의 모듈 폴더를 path에 추가
from module import autopagdd as apd

region_game=[None]*4
resolution = "img"
confi = 0.95
TouchBox = [None]*20
# 윈도우 세팅 및 구역 설정
def set_windowAndRegion(thema,title="BlueStacks App Player"):
    iconfile = apd.whatColorTitlebar(thema)
    print(iconfile)
    while True:
        print("구역설정")
        while True:
            time.sleep(0.1)
            print("구역설정 중..")
            if (apd.bring_to_window(title)): break
        img_icon = pag.locateOnScreen('./' + resolution + '/' + iconfile, confidence=confi, minSearchTime=5)
        if (img_icon):
            temp = [
                img_icon.left,  # left
                img_icon.top,  # top
                1026,  # width
                800,  # height
            ]
            for i in range(len(region_game)): region_game[i] = temp[i]  # region변수에 삽입
            print("구역 설정 완료!" + str(region_game))
            # TouchBox = setTouchRegion(region_game)
            setTouchRegion()
            print("터치 영역 설정 완료!")
            break

def setTouchRegion():
    TouchBox[1] = [
        region_game[0] + 504,
        region_game[1] + 650,
        45,30,
    ]
    TouchBox[2] = [
        region_game[0] + 504,
        region_game[1] + 691,
        45, 30,
    ]
    TouchBox[3] = [
        region_game[0] + 504,
        region_game[1] + 784,
        45, 30,
    ]
    TouchBox[4]= [
        region_game[0] + 324,
        region_game[1] + 628,
        131, 34,
    ]


# always스레드
thread = apd.always("child")
thread.daemon = True
thread.start()

# 변수
print(region_game)
while True:
    if (pag.locateOnScreen("./img/bool.png", confidence=confi)):
        set_windowAndRegion("black")
        while True:
            apd.click_btnTwo(TouchBox[3],duration=0)
            apd.click_btnTwo(TouchBox[1],duration=0)
            #
            apd.click_btnTwo(TouchBox[4], duration=0)
            apd.click_btnTwo(TouchBox[3], duration=0)
            apd.click_btnTwo(TouchBox[2], duration=0)
            #
            apd.click_btnTwo(TouchBox[4], duration=0)