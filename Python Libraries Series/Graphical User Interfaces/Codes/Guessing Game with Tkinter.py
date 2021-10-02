import tkinter as tk
from tkinter import messagebox
random_items = {'numbers': [22,34,55,8,0,102,14,18,21,88],
                'colors':['black','red','eggplant','yellow','beige',
                          'magenta','turquoise','orange','indigo','olive']}
def checkguess():
    user_name = name.get()
    user_guess = guess.get()
    print(user_name,user_guess)
    print(choice.get()==1)
    if choice.get()==1:
        user_guess = int(user_guess)
        if user_guess in random_items['numbers']:
            messagebox.showinfo("Congratulations!", "You guessed correctly!")
            root.quit()
        else:
            messagebox.showerror("Oops!", "You guessed incorrectly. Try again.")
    else:
        user_guess = user_guess.lower()
        if user_guess in random_items['colors']:
            messagebox.showinfo("Congratulations!", "You guessed correctly!")
            root.quit()
        else:
            messagebox.showerror("Oops!", "You guessed incorrectly. Try again.")


root = tk.Tk()
root.geometry("400x400+800+200")

label = tk.Label(root, text="Welcome to Women Who Code Python")
label.place(x=200,y=10,anchor='center')

welcome = tk.Label(root, text="What is your name?")
welcome.place(x=120,y=50,anchor='center')
name = tk.Entry(root)
name.place(x=250,y=50,anchor='center')


choice_label = tk.Label(root,text="What would you like to try your luck at?")
choice_label.place(x=200,y=120,anchor='center')

choice = tk.IntVar()
btn_1 = tk.Radiobutton(root, text="Number", variable=choice, value=1)
btn_1.place(x=100,y=150,anchor='center')
btn_2 = tk.Radiobutton(root, text="Color", variable=choice, value=2)
btn_2.place(x=300,y=150,anchor='center')


guess_label = tk.Label(root, text="Enter your guess here!")
guess_label.place(x=120,y=220,anchor='center')
guess = tk.Entry(root)
guess.place(x=250,y=220,anchor='center')

go_btn = tk.Button(root,text="Let's Go!!",command=checkguess)
go_btn.place(x=200,y=250,anchor='center')



root.mainloop()
