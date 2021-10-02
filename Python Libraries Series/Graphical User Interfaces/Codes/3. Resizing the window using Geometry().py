import tkinter as tk

# create an instance of the Tk()
root = tk.Tk()
root.geometry("200x200+400+300") 
label = tk.Label(root, text="Women Who Code")
label.grid(row=0)

label = tk.Label(root, text="Python")
label.grid(row=1)

root.mainloop()