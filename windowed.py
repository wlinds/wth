import pyautogui
import tkinter as tk

def get_hex():
    x, y = pyautogui.position()
    pixel_color = pyautogui.pixel(x, y)
    hex_color = "#{:02X}{:02X}{:02X}".format(*pixel_color)

    return hex_color

def update_color_label():
    # Update color of window
    color_value = get_hex()
    root.configure(background=color_value)
    root.after(100, update_color_label)

def copy_to_clipboard(event=None):
    # Get current color value and copy it to clipboard
    color_value = get_hex()
    root.clipboard_clear()
    root.clipboard_append(color_value)
    root.update()

if __name__ == "__main__":
    # window with label to display the color value
    root = tk.Tk()
    root.title("What the hex?!")
    color_label = tk.Label(root, text=get_hex(), font=("Arial", 18), padx=20, pady=20)
    color_label.pack()

    # button to copy color to clipboard
    button_0 = tk.Button(root, text="Ctrl+C to copy", command=copy_to_clipboard)
    button_0.pack()
    root.bind("<Control-c>", copy_to_clipboard)

    root.after(100, update_color_label)

    # Start the main event loop
    root.mainloop()