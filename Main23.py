import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        # navBar
        self.menuvar = tk.Menu(self.root)

        self.filemenuu = tk.Menu(self.menuvar, tearoff=0)
        self.filemenuu.add_command(label="Close", command=self.onclosing)
        #adds that line separator
        self.filemenuu.add_separator()
        self.filemenuu.add_command(label="Close without question", command=exit)


        self.actionMenu = tk.Menu(self.menuvar, tearoff=0)
        self.actionMenu.add_command(label="Show Message", command=self.showMessage)



        self.menuvar.add_cascade(menu=self.filemenuu, label="File")
        self.menuvar.add_cascade(menu=self.actionMenu, label="Action")

        # add menubar on top
        self.root.config(menu=self.menuvar)
        # Label
        self.label =tk.Label(self.root, text="Message", font=('Arial', 19))
        self.label.pack(padx=10, pady=10)
        #textBox
        self.textbox = tk.Text(self.root, font=('Arial', 17))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        #CheckBox
        self.check_State = tk.IntVar()

        self.checkBok = tk.Checkbutton(self.root, text= "Show Mssagebox", font=('Arial', 17), variable =self.check_State)
        self.checkBok.pack(padx=10, pady=10)

        #Button
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command= self.showMessage)
        self.button.pack(padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.onclosing)# on close window
        self.clearBtn = tk.Button(self.root, text="Clear", command=self.clear)
        self.clearBtn.pack(padx=10,pady=10)
        self.root.mainloop()


    def showMessage(self):
        # print("Hello World")
        # print(self.check_State.get())# gets the cvurrent state of text  box 1 == true 0 == false
        if self.check_State.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))#basically get the text from start to end


#key shortcut clrt + enter
    def shortcut(self, event):
        # print(event)# basically prints the event
        # print(event.keysym)# basically prints the event
        # print(event.state)# basically prints the event

        if event.state == 4 and event.keysym == "Return":
            self.showMessage()

    #close event
    def onclosing(self):

        if messagebox.askyesno(title="Close", message="Are you sure ?"):

            self.root.destroy()


    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()

