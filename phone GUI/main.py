import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

class App:
    
    def __init__(self, root):
        #setting title
        root.title("tk")
        #setting window size
        width=410
        height=322
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        top_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        top_label["font"] = ft
        top_label["fg"] = "Red"
        top_label["justify"] = "center"
        top_label["text"] = "Contact Info Storage"
        top_label.place(x=90,y=10,width=253,height=32)

        name_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        name_label["font"] = ft
        name_label["fg"] = "#333333"
        name_label["justify"] = "center"
        name_label["text"] = "Name: "
        name_label.place(x=30,y=60,width=104,height=30)

        phone_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        phone_label["font"] = ft
        phone_label["fg"] = "#333333"
        phone_label["justify"] = "center"
        phone_label["text"] = "Phone number: "
        phone_label.place(x=0,y=110,width=107,height=30)

        self.name_box=tk.Entry(root)
        self.name_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.name_box["font"] = ft
        self.name_box["fg"] = "#333333"
        self.name_box["justify"] = "left"
        self.name_box["text"] = ""
        self.name_box.place(x=110,y=60,width=284,height=30)

        self.phone_box=tk.Entry(root)
        self.phone_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.phone_box["font"] = ft
        self.phone_box["fg"] = "#333333"
        self.phone_box["justify"] = "left"
        self.phone_box["text"] = ""
        self.phone_box.place(x=110,y=110,width=285,height=30)

        add_button=tk.Button(root)
        add_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        add_button["font"] = ft
        add_button["fg"] = "Blue"
        add_button["justify"] = "center"
        add_button["text"] = "Add"
        add_button.place(x=260,y=150,width=128,height=30)
        add_button["command"] = self.add_button_command

        remove_button=tk.Button(root)
        remove_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        remove_button["font"] = ft
        remove_button["fg"] = "Blue"
        remove_button["justify"] = "center"
        remove_button["text"] = "Remove"
        remove_button.place(x=260,y=190,width=127,height=30)
        remove_button["command"] = self.remove_button_command

        display_button=tk.Button(root)
        display_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        display_button["font"] = ft
        display_button["fg"] = "Blue"
        display_button["justify"] = "center"
        display_button["text"] = "Display"
        display_button.place(x=260,y=230,width=126,height=30)
        display_button["command"] = self.display_button_command

        exit_button=tk.Button(root)
        exit_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "Red"
        exit_button["justify"] = "center"
        exit_button["text"] = "Exit"
        exit_button.place(x=260,y=270,width=126,height=30)
        exit_button["command"] = self.exit_button_command

    def add_button_command(self):
        name = self.name_box.get()
        phone_num = self.phone_box.get()
        if (not name.isalpha()) or (not phone_num.isnumeric()):
            messagebox.showinfo("Info", "Invalid data format")
            return
        file_object = open('data.txt', 'a')
        file_object.write(name + ": " + phone_num + "\n")
        messagebox.showinfo("Info", "Success")
        file_object.close()


    def remove_button_command(self):
        name = self.name_box.get()
        phone_num = self.phone_box.get()
        flag = True
        with open("data.txt", "r") as f:
            lines = f.readlines()
        with open("data.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != name + ": " + phone_num:
                    f.write(line)
                else:
                    messagebox.showinfo("Info", "Succesfully Removed")
                    flag = False
        if flag:
            messagebox.showinfo("Info", "No such data found")


    def display_button_command(self):
        with open("data.txt", 'r') as f:
            messagebox.showinfo("Data", f.read())


    def exit_button_command(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
