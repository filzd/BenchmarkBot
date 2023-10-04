import pyautogui
import time

def reaction_time(x, y, colour, count):
    while count < 5:
        if pyautogui.pixelMatchesColor(x, y, colour):
            pyautogui.click(x, y)
            time.sleep(0.5)
            pyautogui.click(x, y)
            count += 1
    return "gg"
    
if __name__ == "__main__":
    x, y = 1400, 300
    green = (30, 151, 80)
    count = 0
    reaction_time(x, y, green, count)

