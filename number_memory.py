import pyautogui
import pytesseract
import keyboard

def number_memory():
    while True:
        # fail safe
        if keyboard.is_pressed('q'):
            break
        
        # Capture a screenshot of the specified region
        # TODO: coordinates
        screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))  # Replace with valid coordinates
        
        # Extract text from the screenshot
        numbers = pytesseract.image_to_string(screenshot)
        
        # Remove non-numeric characters
        numbers = ''.join(filter(str.isdigit, numbers))
        
        # If there are numbers, type them and press "Enter"
        if numbers:
            pyautogui.typewrite(numbers)
            pyautogui.press("enter")


if __name__ == "__main__":
    number_memory()