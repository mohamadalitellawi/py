
import tkinter as tk
from tkinter import ttk

from tkinter import messagebox





def click_btn1():
    print("btn1 is clicked")
    a = messagebox.showinfo("Hello World","My first message")
    print (a)
def click_btn2():
    print("btn2 is clicked")
    #root.destroy()
    a = messagebox.askyesno("Hello World","My first message")
    print(a)

def main():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("300x150")

    frame = ttk.Frame(root,padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    btn1 = ttk.Button(frame, text="Click Me", command=click_btn1)
    btn2 = ttk.Button(frame,text="Do Not Click", command=click_btn2)

    btn1.pack()
    btn2.pack(fill=tk.BOTH)

    frm = ttk.Frame(root,padding="10 10 10 10")
    frm.pack(fill=tk.BOTH, expand=True)
    invText = tk.StringVar()
    invEntry = ttk.Entry(frm,width=25,textvariable=invText,state="readonly")
    invEntry.pack()
    invText.set("Hello Dear")
    root.mainloop()

if __name__ == "__main__":
    main()