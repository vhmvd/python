import tkinter as tk
from tkinter.constants import INSERT
from typing import Text
from file import file_read

class gui:
  def __init__(self):
    """Contructor
    """
    self.data = file_read()
    self.data.file_read()
  def create_gui(self):
    """Creates tkinter GUI from available methods
    Root initialise the object
    """
    self.root = tk.Tk()
    """Sets title of the GUI
    """
    self.root.title("London Underground Journey Planner")

    """Loads background image
    """
    background_image_file = "lts.png"

    """Sets the windows height and width according to image
    """
    bg_image = tk.PhotoImage(file = background_image_file)
    h = bg_image.height()
    w = bg_image.width()
    self.root.geometry("%dx%d+50+30" % (w, h))
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')

    """For creation of input box and adding a name label for them
    """
    label_start_station = tk.Label(self.root, text="Starting station", fg="blue")
    label_end_station   = tk.Label(self.root, text="Ending station"  , fg="blue")
    label_time          = tk.Label(self.root, text="Time")
    self.start_station  = tk.Entry(self.root)
    self.end_station    = tk.Entry(self.root)
    self.time           = tk.Entry(self.root)

    """Aligns the floating properties on the GUI
    """
    label_start_station.place(x=130, y=100)
    label_end_station  .place(x=440, y=100)
    label_time         .place(x=310, y=100)
    self.start_station .place(x=110, y=125)
    self.end_station   .place(x=420, y=125)
    self.time          .place(x=265, y=125)

    """Creates Buttons on the GUI
    """
    submit_button = tk.Button(self.root, text="Submit", fg="green", command=self.store_data)
    quit_button   = tk.Button(self.root, text="Quit"  , fg="red"  , command=self.root.destroy)
    """Aligns the button on GUI
    """
    submit_button.place(x=330, y=150)
    quit_button  .place(x=280, y=150)

    self.root.mainloop()

  def store_data(self):
    """Is invoked at the press of submit button from GUI and passes the information to algorithm for computation
    """
    self.sst = self.start_station.get().title() 
    self.est = self.end_station.get().title()
    try:
      self.data.create_nodes()
      self.path = self.data.algorithm(self.sst, self.est, self.time.get())
      data = "time\ttotal\tline\tstation\n"
      total = 0
      for itr in self.path:
        total += itr[2]
        data = data + str(itr[2])+"min" +"\t" +str(total)+"min"+"\t" + itr[0] +"\t"+ itr[1]
        data = data+ "\n"
      self.win = tk.Tk()
      text = tk.Text(self.win, height=50, width=100)
      text.pack()
      text.insert(tk.END, data)
      self.win.mainloop()
    except:
      self.data.create_nodes_again()
      self.path2 = self.data.algorithm(self.est, self.sst, self.time.get())
      data = "time\ttotal\tline\tstation\n"
      total = 0
      for itr in reversed(self.path2):
        total += itr[2]
        data = data + str(itr[2])+"min" +"\t" +str(total)+"min"+"\t" + itr[0] +"\t"+ itr[1]
        data = data+ "\n"
      self.win = tk.Tk()
      text = tk.Text(self.win, height=50, width=100)
      text.pack()
      text.insert(tk.END, data)
      self.win.mainloop()
  
a = gui()
a.create_gui()
