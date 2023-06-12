import tkinter as tk

root = tk.Tk()# basically main window constructor

root.geometry("800x600") # set resolution x,y value
root.title("FirstGui")# sets the Title

label = tk.Label(root, text="Label Inside GUI", font=('Arial', 20))

label.pack(padx=20, pady=30)# set padding basically

# textBox w/ Parameters
textbox = tk.Text(root, height=3, font= ('Arial', 16))
textbox.pack(padx=10)
myentry = tk.Entry(root)
myentry.pack(pady=10)

myButton = tk.Button(root, text="ClickButton", font=("Arial", 20))
myButton.pack(padx=10, pady=10)


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)
buttonFrame.columnconfigure(4, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 19))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)# basically means first column

btn2 = tk.Button(buttonFrame, text="2", font=('Arial', 19))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)# basically means first column

btn3 = tk.Button(buttonFrame, text="3", font=('Arial', 19))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)# basically means first column

btn4 = tk.Button(buttonFrame, text="4", font=('Arial', 19))
btn4.grid(row=0, column=3, sticky=tk.W + tk.E)# basically means first column

btn5 = tk.Button(buttonFrame, text="5", font=('Arial', 19))
btn5.grid(row=0, column=4, sticky=tk.W + tk.E)# basically means first column

btn6 = tk.Button(buttonFrame, text="6", font=('Arial', 19))
btn6.grid(row=1, column=0, sticky=tk.W + tk.E)# basically means first column

btn7 = tk.Button(buttonFrame, text="7", font=('Arial', 19))
btn7.grid(row=1, column=1, sticky=tk.W + tk.E)# basically means first column

btn8 = tk.Button(buttonFrame, text="8", font=('Arial', 19))
btn8.grid(row=1, column=2, sticky=tk.W + tk.E)# basically means first column


buttonFrame.pack(fill ="x", pady=30)

anotherButton = tk.Button(root, text="Another ONe")
anotherButton.place(x=400,y=100, height=200, width=100)# basically custom Place
#make sure stuf go above the main loop
root.mainloop() # call the constructor

