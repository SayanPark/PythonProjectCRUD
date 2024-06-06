from tkinter import Label, Button, Toplevel, PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import SYN_DO


def showlistwin():
    # showlist form(design)
    win = Toplevel()
    win.title('showlist')
    win.geometry('300x200')
    win.resizable(False, False)
    win.config()
    win.iconbitmap('document.ico')
    # showlist form(buttons)
    btn_img = PhotoImage(file='add.png')
    Button(win, image=btn_img, command=SYN_DO.add).place(x=50, y=40)
    btn_img2 = PhotoImage(file='delete.png')
    Button(win, image=btn_img2, command=SYN_DO.delete).place(x=50, y=110)
    btn_img3 = PhotoImage(file='edit.png')
    Button(win, image=btn_img3, command=SYN_DO.edit).place(x=200, y=40)
    btn_img4 = PhotoImage(file='showlist.png')
    Button(win, image=btn_img4, command=SYN_DO.search).place(x=200, y=110)
    # showlist form(labels)
    Label(win, text='add employees').place(x=30, y=82)
    Label(win, text='delete employees').place(x=30, y=152)
    Label(win, text='edit employees').place(x=180, y=82)
    Label(win, text='search employees').place(x=180, y=152)
    win.mainloop()


def showlistcashwin():
    # showlist form(design)
    win = Toplevel()
    win.title('showlist')
    win.geometry('600x500')
    win.resizable(False, False)
    win.config()
    win.iconbitmap('document.ico')
    # showlist form(labels)
    Label(win, text='add employees').place(x=120, y=20)
    # showlist form(method)
    with open('List_of_employees.txt', 'r') as f:
        lines = f.readlines()
        salaries = []
        lastnames = []
        for i, line in enumerate(lines):
            if line.startswith('Last name: '):
                lastnames.append(line.split('Last name: ')[1].strip())
            if line.startswith('Salary: ') and line.endswith(',000,000\n'):
                salary_str = line.split('Salary: ')[1].replace(',', '').strip()
                salaries.append(int(salary_str))
        average = sum(salaries) / len(salaries) / 1_000_000
        fig, ax = plt.subplots()
        ax.bar(lastnames, salaries)
        ax.set_xlabel('Last Names')
        ax.set_ylabel('Salaries (in millions)')
        ax.set_title('Employee Salaries')
        ax.text(0.4, 1.1, f'Average Salary: {average: .2f} milion', transform=ax.transAxes, ha='right')
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side='top', fill='both', expand=1)
    win.mainloop()
