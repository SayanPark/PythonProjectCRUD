from tkinter import Label, Button, Toplevel, PhotoImage


def success():
    # success form(design)
    winsu = Toplevel()
    winsu.title('success')
    winsu.geometry('200x100')
    winsu.resizable(False, False)
    winsu.config()
    winsu.iconbitmap('document.ico')
    # success form(labels)
    btn_img = PhotoImage(file='success.png')
    Label(winsu, image=btn_img).place(x=25, y=25)
    Label(winsu, text='mission complete').place(x=60, y=30)
    # success form(button)
    Button(winsu, text='Exit', command=winsu.destroy).place(x=160, y=60)
    winsu.mainloop()


def error():
    # error form(design)
    winer = Toplevel()
    winer.title('ERROR')
    winer.geometry('200x100')
    winer.resizable(False, False)
    winer.config()
    winer.iconbitmap('document.ico')
    # error form(labels)
    btn_img = PhotoImage(file='warning.png')
    Label(winer, image=btn_img).place(x=20, y=25)
    Label(winer, text='the value is incorrect').place(x=55, y=35)
    # error form(button)
    Button(winer, text='OK', command=winer.destroy).place(x=160, y=60)
    winer.mainloop()
