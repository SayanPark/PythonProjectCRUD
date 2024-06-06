from tkinter import Tk, Label, Button, PhotoImage, messagebox
import SYN_list
# design of main form
win = Tk()
win.title('Final programming')
win.geometry('500x250')
win.resizable(False, False)
win.iconbitmap('document.ico')
win.overrideredirect(True)


def exitt():
    # quit form(design)
    if messagebox.askokcancel('Exit', 'Want to exit?'):
        win.destroy()


# exit button codes
btn_img = PhotoImage(file='exit.png')
Button(win, image=btn_img, command=exitt).place(x=400, y=170)
Label(win, text='Exit').place(x=407, y=210)
# employees button codes
btn_img2 = PhotoImage(file='document.png')
Button(win, image=btn_img2, command=SYN_list.showlistwin).place(x=140, y=85)
Label(win, text='Employees').place(x=130, y=125)
# salaries button codes
btn_img3 = PhotoImage(file='money.png')
Button(win, image=btn_img3, command=SYN_list.showlistcashwin).place(x=310, y=85)
Label(win, text='Salary').place(x=310, y=125)
win.mainloop()
