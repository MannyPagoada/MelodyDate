import tkinter as tk
from tkinter import Toplevel


#function for pop up to verify that i got the string and button
def showInput():
    s = userInput.get()

    popUP = Toplevel(window)
    popUP.title("TEST")

    label = tk.Label(popUP, text="The date given is {}".format(s))
    label.pack()



window=tk.Tk()

#window.geometry("800x500")
window.title("Melody Maker")

label = tk.Label(window, text="MelodyMaker", font=('Arial', 18))
label.pack(padx=10, pady=10)

label1=tk.Label(window, text="This application is designed to take any date and make an orginal song using machine learning. Give it a try!", font=('Arial', 12),padx=10, pady=10)
label1.pack()

userInput=tk.Entry(window)
userInput.pack()

submit=tk.Button(window, text='Submit!', font=('Arial', 8), command=showInput)
submit.pack(pady=10)



window.mainloop()