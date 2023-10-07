import pyautogui
import pytesseract
import keyboard

def verbal_memory():
    # start
    pyautogui.click(x=1270, y=560)
    
    # list of seen words
    seen = []
    
    while True:
        # fail safe
        if keyboard.is_pressed("q"):
            break
        
        # get the word using screenshot
        pyautogui.screenshot()
        screenshot = pyautogui.screenshot(region=(1000, 365, 1537, 437))
        screenshot = pyautogui.screenshot("word.png")
        word = pytesseract.image_to_string("word.png")
        
        # if seen
        if word in seen:
            pyautogui.click(x=1200, y=480)
        # if not seen
        elif word not in seen:
            pyautogui.click(x=1337, y=480)
            seen.append(word)


if __name__ == "__main__":
    verbal_memory()