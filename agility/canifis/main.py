import pyautogui
import random
import psutil 

resetFailures = 0

def Reset():
    global resetFailures
    print('--------------------')
    print("Resetting back to start")

    for i in range(1, 5):
        print(f'Searching for start #{i}')
        tileCoords = pyautogui.locateCenterOnScreen(f'./start_{i}.png', confidence=0.8 if i == 1 else 0.4)
        
        if tileCoords is None:
            print(f'Could not find start #{i}')
            pyautogui.sleep(5 + random.uniform(0, 2))

            # Exit script if fail too many times in succession
            if resetFailures == 3:
                return
            resetFailures = resetFailures + 1
            Reset()
            return
        
        print(f'Found start #{i}')
        pyautogui.leftClick(tileCoords[0] + random.randrange(-3, 3), tileCoords[1] + random.randrange(-3, 3))
        if i == 4: # long tree animation
            pyautogui.sleep(7 + random.uniform(0, 2))
        else:
            pyautogui.sleep(5 + random.uniform(0, 2))

    resetFailures = 0
    Traverse()

def Traverse():
    while(1):
        print('--------------------')
        for i in range(1, 9):
            print(f'Searching for mark')
            markCoords = pyautogui.locateCenterOnScreen(f'./mark.png', confidence=0.6)
            if markCoords is not None:
                print(f'Found mark')
                markX = markCoords[0] + random.randrange(-10, 10)
                markY = markCoords[1] + random.randrange(-10, 10)

                pyautogui.moveTo(markX, markY)
                pyautogui.leftClick(markX, markY)
                pyautogui.sleep(6)

            print(f'Searching for building #{i} exit ')
            buildingCoords = pyautogui.locateCenterOnScreen(f'./building_{i}_exit.png', confidence=0.5)

            # edge case
            if i == 2 and buildingCoords is None:
                print(f'Searching for building #{i}_2 exit ')
                buildingCoords = pyautogui.locateCenterOnScreen(f'./building_{i}_2_exit.png', confidence=0.5)

            if buildingCoords is None:
                print("Could not find building exit")
                Reset()
                return

            print(f'Found building #{i} exit')
            # pyautogui.moveTo(buildingCoords[0] + random.randrange(-10, 10), buildingCoords[1] + random.randrange(-10, 10))
            pyautogui.leftClick(buildingCoords[0] + random.randrange(-10, 10), buildingCoords[1] + random.randrange(-10, 10))
            if i == 6 or i == 7: # large building, long tree animation
                pyautogui.sleep(9 + random.uniform(0, 2))
            else:
                pyautogui.sleep(7 + random.uniform(0, 2))
    return

def Main():
    print('Looking for running HDOS application')   
    if "HDOS.exe" not in (p.name() for p in psutil.process_iter()):
        print("HDOS not running, exiting")
        return
    print('Please switch focus to HDOS now')

    print('Resetting camera position in 5 seconds')
    pyautogui.sleep(5)
    centerMap = pyautogui.locateCenterOnScreen(f'./center-map.png', confidence=0.5)
    pyautogui.leftClick(centerMap[0] + random.randrange(-3, 3), centerMap[1] + random.randrange(-3, 3))
    pyautogui.moveTo(500, 500)
    pyautogui.dragTo(500, 700, 2, button='middle')
    pyautogui.scroll(100000) # zoom all the way in
    pyautogui.sleep(1 + random.uniform(0, 1))
    pyautogui.scroll(-2500)

    Reset()
Main()