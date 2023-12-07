import subprocess
import re, os
import time
import keyboard
import matplotlib.pyplot as plt
print(os.getcwd())
#상수
MIN_X = 0
MIN_Y = 0
MAX_X = 32776
MAX_Y = 32776

displayWidth = 900 + 1
displayHeight = 1600 + 1

time_cycle = 60
time_end = 600

def convertToRealPoint(point):
    x,y = point
    displayX = (x - MIN_X) * displayWidth / (MAX_X - MIN_X + 1)
    displayY = (y - MIN_Y) * displayHeight / (MAX_Y - MIN_Y + 1)
    # displayY = displayHeight-1 - displayY
    return [int(displayX),int(displayY)]

def drawGraph():
    # 그래프 그리기
    x_coords = [x for [x, y] in touch_events]
    y_coords = [y for [x, y] in touch_events]

    plt.figure(figsize=(5,10))
    plt.scatter(x_coords, y_coords, color='black', s=1)
    plt.title('Touch Coordinates')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.xlim(0,displayWidth-1)
    plt.ylim(0,displayHeight-1)

    plt.show()

def saveTouchEventsToFile(touch_events, file_index):
    with open(f"touch_events_log_{file_index}.txt", "w") as file:
        for event in touch_events:
            file.write(f'{event}\n')
        print(f"Touch events saved to file touch_events_log_{file_index}.txt.\n\n\n")

def loadTouchEventsFromFile(filename):
    loaded_touch_events = []
    with open(filename, "r") as file:
        for line in file:
            values = line.strip()[1:-1].split(", ")
            loaded_touch_events.append([int(values[0]), int(values[1])])
    print(loaded_touch_events)
    return loaded_touch_events

os.chdir("./platform-tools")
# Device identifier
device_id = "emulator-5554"  # Replace with your device identifier
# device_id = "HA1R60JW"  # Replace with your device identifier

# ADB command with device identifier
command = f"adb -s {device_id} shell getevent -l"

# Running the ADB command and retrieving output
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Extracting touch coordinates from the output
touch_events = []
file_index= 0
boolTime = True
os.chdir("./..")
for line in iter(process.stdout.readline, b''):

    if boolTime:
        start_time = time.time()
        boolTime = False
    
    line = line.decode("utf-8").strip()
    if "ABS_MT_POSITION_X" in line:
        x_hex = re.findall(r'([0-9a-fA-F]{8})$', line)[0]
        current_coordinates = [int(x_hex, 16)]
    elif "ABS_MT_POSITION_Y" in line and current_coordinates is not None:
        y_hex = re.findall(r'([0-9a-fA-F]{8})$', line)[0]
        current_coordinates.append(int(y_hex, 16))
        print(f"{current_coordinates} to {convertToRealPoint(current_coordinates)}")
        # touch_events.append(convertToRealPoint(current_coordinates))
        touch_events.append(current_coordinates)
        current_coordinates = None
    if keyboard.is_pressed('F12'):
        print("exit")
        saveTouchEventsToFile(touch_events, "test")
        break
    #한사이클 종료 시
    # if (time.time() - start_time) > time_cycle:
    #     start_time = time.time() # 초기화
    #     file_index += 1
    #     saveTouchEventsToFile(touch_events,file_index)
    #     touch_events = []

    if (time.time() - start_time) > time_end:
        saveTouchEventsToFile(touch_events, "test")
        break
