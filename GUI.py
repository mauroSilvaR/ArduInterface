import serial
import tkinter as tk

GRID_ROWS = 8
GRID_COLUMNS = 8

# List to hold the buttons
buttons = []

# helper functions --------------------------------------------------------
def create_grid_of_buttons():
    for j in range(GRID_ROWS):
        row_buttons = []
        for i in range(GRID_COLUMNS):
            btn = tk.Button(frame_buttons, bg="white",
                            command=lambda i=i, j=j: on_button_click(i, j))
            btn.grid(row=j, column=i, padx=2, pady=2)
            row_buttons.append(btn)
        buttons.append(row_buttons)
# -------------------------------------------------------------------------


# Handler functions for the tkinter objects---------------------------------------

#handler function for a matrix button click
def on_button_click(i, j):
    btn = buttons[j][i]
    current_color = btn.cget("bg")
    new_color = "red" if current_color == "white" else "white"
    btn.config(bg=new_color)
    # at this momento we know exactly which button we are pressing

#handler function for the reset button
def reset_grid():
    for i in range(0,GRID_ROWS):
        for j in range (0,GRID_COLUMNS):
            btn = buttons[j][i]
            new_color = "white"
            btn.config(bg=new_color)
            status_label.config(text=f"All buttons reset!")

#handler function for the send button
def send_command():
    print("here is where I'll process the conversion and formatting to UART\n")
# End of Handler functions for the tkinter objects---------------------------------------



# Main window
root = tk.Tk()
root.title("ArduInterface")

# Frame for the matrix buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Creating the grid of buttons
create_grid_of_buttons()

# Frame for reset button, label and send button
frame_status = tk.Frame(root)
frame_status.pack(pady=10)

# create the reset button
reset_button = tk.Button(frame_status,
                         text="Reset",
                         command=reset_grid)
reset_button.grid(row=0,column=0)
# create the label
status_label = tk.Label(frame_status, text="Click on the buttons to change their state")
status_label.grid(row=0,column=1)
# create the send button
send_button = tk.Button(frame_status,
                        text = "Send!",
                        command=send_command)
send_button.grid(row=0,column=2)


# Start the main loop!
root.mainloop()


