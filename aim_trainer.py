import pyautogui
import keyboard

def aim_trainer():
    pyautogui.PAUSE = 0.1
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting program...")
            break
        search_region = (776, 134, 1748, 672) 
        target_location = pyautogui.locateOnScreen('target.png', region=search_region, confidence=0.8)
        
        if target_location is not None:
            target_x, target_y = pyautogui.center(target_location)
            pyautogui.click(target_x, target_y)
        
if __name__ == "__main__":
    aim_trainer()
