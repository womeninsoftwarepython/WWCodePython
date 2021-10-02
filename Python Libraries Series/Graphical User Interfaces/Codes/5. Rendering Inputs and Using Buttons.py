import tkinter as tk

def addNetwork():
    network = entry.get()
    network_label = tk.Label(root,text=network)
    network_label.place(x=150,y=40,anchor='center')
# create an instance of the Tk()
root = tk.Tk()
root.geometry("300x300") #+400+300
label = tk.Label(root, text="Women Who Code")
label.place(x=150,y=20,anchor='center')
entry = tk.Entry(root)
entry.place(x=100,y=100,anchor='center')

addnetwork_btn = tk.Button(root, text="Add Network",command=addNetwork)
addnetwork_btn.place(x=250,y=100,anchor='center')

root.mainloop()