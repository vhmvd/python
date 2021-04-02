import tkinter as tk
import tkinter.font as tkFont

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class App:
    def __init__(self, root):
        #setting title
        root.title("MPG Calculator")
        #setting window size
        width=271
        height=322
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        top_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        top_label["font"] = ft
        top_label["fg"] = "#ff0000"
        top_label["justify"] = "center"
        top_label["text"] = "Miles per gallon calculator"
        top_label.place(x=10,y=10,width=253,height=32)

        fuel_tank_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        fuel_tank_label["font"] = ft
        fuel_tank_label["fg"] = "#333333"
        fuel_tank_label["justify"] = "center"
        fuel_tank_label["text"] = "Fuel tank capacity:"
        fuel_tank_label.place(x=20,y=110,width=108,height=30)

        range_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        range_label["font"] = ft
        range_label["fg"] = "#333333"
        range_label["justify"] = "center"
        range_label["text"] = "Range on full tank:"
        range_label.place(x=20,y=150,width=107,height=30)

        self.fuel_tank_input_box=tk.Entry(root)
        self.fuel_tank_input_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.fuel_tank_input_box["font"] = ft
        self.fuel_tank_input_box["fg"] = "#333333"
        self.fuel_tank_input_box["justify"] = "center"
        self.fuel_tank_input_box["text"] = ""
        self.fuel_tank_input_box.place(x=130,y=110,width=129,height=30)

        self.range_input_box=tk.Entry(root)
        self.range_input_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.range_input_box["font"] = ft
        self.range_input_box["fg"] = "#333333"
        self.range_input_box["justify"] = "center"
        self.range_input_box["text"] = ""
        self.range_input_box.place(x=130,y=150,width=128,height=30)

        calculate_button=tk.Button(root)
        calculate_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        calculate_button["font"] = ft
        calculate_button["fg"] = "#0000ff"
        calculate_button["justify"] = "center"
        calculate_button["text"] = "Calculate"
        calculate_button.place(x=130,y=190,width=128,height=30)
        calculate_button["command"] = self.calculate_button_command

        self.result_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.result_label["font"] = ft
        self.result_label["fg"] = "#008000"
        self.result_label["justify"] = "center"
        self.result_label["text"] = ""
        self.result_label.place(x=20,y=260,width=221,height=30)

    def calculate_button_command(self):
        range_var = self.range_input_box.get()
        capacity_var = self.fuel_tank_input_box.get()
        if is_float(str(range_var)) and is_float(str(capacity_var)):
            result_var = float(range_var) / float(capacity_var)
            self.result_label["text"] = "MPG = " + str(result_var)
            self.result_label["fg"] = "#008000"
        else:
            self.result_label["text"] = "Invalid entries!!"
            self.result_label["fg"] = "Red"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
