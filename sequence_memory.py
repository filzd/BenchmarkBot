import pyautogui
import time
import keyboard

def sequence_memory():
   positions = [
       (1137, 299),
       (1272, 299),
       (1407, 299),
       
       (1137, 437),
       (1272, 437),
       (1407, 437),
       
       (1137, 570),
       (1272, 570),
       (1407, 570),
   ]
   
   click_positions = []
   flash_time = None
   
   while True:
        if keyboard.is_pressed('q'):
           print("Exiting program...")
           break
       
        for position in positions:
            if pyautogui.pixelMatchesColor(position[0], position[1], (24, 26, 27)):
                
                if len(click_positions) == 0 or click_positions[-1] != position:
                    flash_time = time.time()
                    click_positions.append(position)

            if flash_time and (time.time() - flash_time) >= 3:
                for click_pos in click_positions:
                    pyautogui.click(click_pos[0], click_pos[1])
                
                click_positions.clear()
                flash_time = None


if __name__ == "__main__":
    sequence_memory()