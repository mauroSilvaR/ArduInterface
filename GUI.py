
import tkinter as tk

def on_button_click(i):
    # Update label when button is clicked
    status_label.config(text=f"You clicked{i}")

# Create main Window
root = tk.Tk()
root.title("ArduInterface")

# Frame for buttons, maybe change to grid later
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# button creation, after mvp can be better, for now, use for
for i in range(1, 8): 
    btn = tk.Button(frame_buttons, text=f"LED {i}", width=10,
                    command=lambda i=i: on_button_click(i))
    btn.pack(side="left", padx=5)

# Frame for message
frame_status = tk.Frame(root)
frame_status.pack(pady=10)

status_label = tk.Label(frame_status, text="Click on the buttons")
status_label.pack()

# Inicia o loop da interface
root.mainloop()

