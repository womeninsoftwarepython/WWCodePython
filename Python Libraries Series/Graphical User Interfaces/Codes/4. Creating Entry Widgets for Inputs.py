import tkinter as tk

# create an instance of the Tk()
root = tk.Tk()
root.geometry("200x200") #+400+300
label = tk.Label(root, text="Women Who Code")
label.pack()

label = tk.Entry(root)
label.pack()

root.mainloop()