import pyautogui
import time

def get_hex():

    x, y = pyautogui.position()
    pixel_color = pyautogui.pixel(x, y)

    hex_color = "#{:02X}{:02X}{:02X}".format(*pixel_color)

    return hex_color

if __name__ == "__main__":
    previous_color = None
    
    while True:
        hex_color = get_hex()

        if hex_color != previous_color:
            print(hex_color)
            previous_color = hex_color
        
        time.sleep(0.1)