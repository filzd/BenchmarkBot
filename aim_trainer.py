import pyautogui
import time
import keyboard
import random

def aim_trainer():
    pyautogui.PAUSE = 0.001
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting program...")
            break
        
        search_region = (776, 134, 1748, 672)  # Adjust coordinates as needed
        confidence_threshold = 0.6  # Adjust confidence as needed
        
        target_location = pyautogui.locateOnScreen('target.png', region=search_region, confidence=confidence_threshold)
        
        if target_location is not None:
            target_x, target_y = pyautogui.center(target_location)
            pyautogui.click(target_x, target_y)
        
        # Minimize sleep time between iterations
        time.sleep(0.001)  # Sleep for 1 millisecond or adjust as needed

if __name__ == "__main__":
    aim_trainer()
