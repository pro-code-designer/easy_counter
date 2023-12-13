import tkinter as tk
import keyboard

root = tk.Tk()

# Set the title of the window
root.title("Transparent Background")

# Set the size of the window
root.geometry("100x50")

# Make the window transparent
root.overrideredirect(True)
root.attributes("-transparentcolor", "white")

# Create a canvas with a transparent background
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Add widgets to the canvas
label = tk.Label(canvas, text="0", font=("Arial", 24), bg="#004252")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def add_one():
    value = int(label.cget("text"))
    value += 1
    label.config(text=str(value))


def sub_one():
    value = int(label.cget("text"))
    value -= 1
    label.config(text=str(value))

def close_window():
    root.destroy()

# Register the global hotkey Control-*
keyboard.add_hotkey("ctrl+*", add_one)
keyboard.add_hotkey("ctrl+/", sub_one)
keyboard.add_hotkey("ctrl+-", close_window)
root.mainloop()
