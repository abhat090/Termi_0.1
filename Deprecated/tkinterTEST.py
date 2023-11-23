from tkinter import *

root = Tk()
root.title("Termi's Terminal:")
root.geometry("700x700")

#print commands for cat
my_list=["Options: ", "1. Cat Dance ", "2. Feed Cat ", "3. Have the Cat Talk "]

txt_output = Text(root, height=5, width=60)
txt_output.pack(pady=30)

for item in my_list:
    txt_output.insert(END, item + "\n")

#create clear function
def clear():
    inputWrite.delete(1.0, END)

def GET_TEXT():
    my_label.config(text=inputWrite.get(1.0, END))

inputWrite = Text(root, width=60, height=20)
inputWrite.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

#get text button
print_text_button = Button(button_frame, text="Print Text", command=GET_TEXT)
print_text_button.grid(row=0, column=1, padx=5)

my_label = Label(root, text='')
my_label.pack(pady=20)

#button to clear screen
clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0, padx=5)

#button for closing
Exit_button = Button(button_frame, text="Exit", command=root.destroy)
Exit_button.grid(row=0, column=2, padx=5)


root.mainloop()