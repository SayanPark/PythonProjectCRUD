from tkinter import StringVar, Label, Entry, Button, Toplevel, IntVar, messagebox
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
import SYN_WES


def add():
    # design for add form
    win = Toplevel()
    win.title('Add employees')
    win.geometry('200x450')
    win.resizable(False, False)
    win.config()
    win.iconbitmap('document.ico')
    # add form(Entries)
    idd = Entry(win)
    idd.place(x=30, y=40)
    fname = Entry(win)
    fname.place(x=30, y=80)
    lname = Entry(win)
    lname.place(x=30, y=120)
    pnum = Entry(win)
    pnum.place(x=30, y=200)
    address = Entry(win)
    address.place(x=30, y=240)
    # add form(radiobutton)
    rd = StringVar()
    gender = ['Male', 'Female']
    Radiobutton(win, text='Female', variable=rd, value=gender[1]).place(x=90, y=160)
    Radiobutton(win, text='Male', variable=rd, value=gender[0]).place(x=30, y=160)
    # add form(labels)
    Label(win, text='ID:').place(x=30, y=20)
    Label(win, text='First name:').place(x=30, y=60)
    Label(win, text='Last name:').place(x=30, y=100)
    Label(win, text='Gender:').place(x=30, y=140)
    Label(win, text='Phone number:').place(x=30, y=180)
    Label(win, text='Address:').place(x=30, y=220)
    Label(win, text='Salary:').place(x=30, y=260)
    Label(win, text='Language:').place(x=30, y=300)
    # add form(combobox)
    cb = StringVar()
    cmb_values = ['Select', '1,000,000',
                     '2,000,000', '3,000,000',
                     '4,000,000', '5,000,000',
                     '6,000,000', '7,000,000',
                     '8,000,000', '9,000,000',
                     '10,000,000']
    cmb = Combobox(win, textvariable=cb, values=cmb_values, state='readonly')
    cmb.place(x=30, y=280)
    cmb.current(0)
    # add form(checkbutton)
    ch1 = StringVar()
    Checkbutton(win, text='Persian', variable=ch1, onvalue='Persian', offvalue=None).place(x=30, y=340)
    ch2 = StringVar()
    Checkbutton(win, text='English', variable=ch2, onvalue='English', offvalue=None).place(x=30, y=360)
    ch3 = StringVar()
    Checkbutton(win, text='Turkish', variable=ch3, onvalue='Turkish', offvalue=None).place(x=30, y=380)
    ch4 = IntVar()

    def selectall():
        if ch4.get() == 1:
            ch1.set('Persian')
            ch2.set('English')
            ch3.set('Turkish')
        else:
            ch1.set('')
            ch2.set('')
            ch3.set('')
    Checkbutton(win, text='Select all', command=selectall, variable=ch4).place(x=30, y=320)
    # add form(method)

    def add_employ():
        try:
            f = open('List_of_employees.txt', 'a')
            f.write(f'id: {int(idd.get())}\nName: {str(fname.get())}\nLast name: {str(lname.get())}\n'
                    f'Gender: {str(rd.get())}\nTelephone: {str(pnum.get())}\nAddress: {str(address.get())}\n'
                    f'Salary: {cmb.get()}\nLanguage: {str(ch1.get()), str(ch2.get()), str(ch3.get())}\n-\n')
        except:
            SYN_WES.error()
        else:
            f.close()
            idd.delete(0, 'end')
            fname.delete(0, 'end')
            lname.delete(0, 'end')
            rd.set('')
            pnum.delete(0, 'end')
            address.delete(0, 'end')
            cmb.current(0)
            ch1.set('')
            ch2.set('')
            ch3.set('')
            ch4.set(0)
    # add form(Button)
    Button(win, text='OK', command=lambda: [add_employ(), SYN_WES.success()]).place(x=150, y=400)
    win.mainloop()


def delete():
    # design for delete form
    win = Toplevel()
    win.title('Delete employees')
    win.geometry('300x70')
    win.resizable(False, False)
    win.config()
    win.iconbitmap('document.ico')
    # delete form(Entries)
    idd = Entry(win)
    idd.place(x=90, y=20)
    # delete form(labels)
    Label(win, text='Enter the ID:').place(x=20, y=20)
    # delete form(method)

    def delete_employ():
        try:
            value = str(idd.get())
            confirm_result = messagebox.askokcancel('Confirmation', 'Are you sure?')
            if confirm_result:
                with open('List_of_employees.txt', 'r') as f:
                    lines = f.readlines()
                new_lines = []
                lines_to_exclude = 0
                found = False
                for line in lines:
                    if value not in line and lines_to_exclude == 0:
                        new_lines.append(line)
                    elif value in line:
                        found = True
                        lines_to_exclude = 9
                    if lines_to_exclude > 0:
                        lines_to_exclude -= 1
                if found:
                    with open('List_of_employees.txt', 'w') as file:
                        file.writelines(new_lines)
                    messagebox.showinfo('Success', 'Employee deleted successfully.')
                else:
                    messagebox.showinfo('Error', 'ID not found.')
            else:
                messagebox.showinfo('Operation Canceled', 'Deletion canceled.')
        except Exception as e:
            messagebox.showerror('Error', str(e))
    Button(win, text='OK', command=delete_employ).place(x=220, y=20)
    win.mainloop()


def edit():
    # design for edit form
    win = Toplevel()
    win.title("Employee Editor")
    win.resizable(False, False)
    win.config()
    win.iconbitmap('document.ico')
    # edit form(values)
    idd = StringVar()
    fname = StringVar()
    lname = StringVar()
    pnum = StringVar()
    address = StringVar()
    rd = StringVar()
    cmb = StringVar()
    gender = ['Male', 'Female']
    cmb_values = ['Select', '1,000,000',
                  '2,000,000', '3,000,000',
                  '4,000,000', '5,000,000',
                  '6,000,000', '7,000,000',
                  '8,000,000', '9,000,000',
                  '10,000,000']
    languagesv = ['Persian', 'English', 'Turkish']
    # edit form(buttons)
    b1 = Button(win, text='Search', command=lambda: search_employee(idd, fname, lname, pnum, address, rd))
    b1.grid(row=12, column=1)
    b2 = Button(win, text='OK', command=lambda: update_employee(idd, fname, lname, pnum, address, rd, cb),
                   state='disabled')
    b2.grid(row=12, column=0)
    # edit form(labels)
    Label(win, text='ID:').grid(row=0, column=0)
    Label(win, text='First Name:').grid(row=1, column=0)
    Label(win, text='Last Name:').grid(row=2, column=0)
    Label(win, text="Gender:").grid(row=3, column=0)
    Label(win, text='Telephone:').grid(row=4, column=0)
    Label(win, text='Address:').grid(row=5, column=0)
    Label(win, text='Salary:').grid(row=6, column=0)
    Label(win, text='Language:').grid(row=7, column=0)
    # edit form(entries)
    id_entry = Entry(win, textvariable=idd)
    id_entry.grid(row=0, column=1)
    fname_entry = Entry(win, textvariable=fname, state='disabled')
    fname_entry.grid(row=1, column=1)
    lname_entry = Entry(win, textvariable=lname, state='disabled')
    lname_entry.grid(row=2, column=1)
    pnum_entry = Entry(win, textvariable=pnum, state='disabled')
    pnum_entry.grid(row=4, column=1)
    address_entry = Entry(win, textvariable=address, state='disabled')
    address_entry.grid(row=5, column=1)
    # edit form(radiobuttons)
    rd_male_radiobutton = Radiobutton(win, text='Male', variable=rd, value=gender[0], state='disabled')
    rd_male_radiobutton.grid(row=3, column=1)
    rd_female_radiobutton = Radiobutton(win, text='Female', variable=rd, value=gender[1], state='disabled')
    rd_female_radiobutton.grid(row=3, column=2)
    # edit form(combobox)
    cmb = Combobox(win, values=cmb_values, state='disabled')
    cmb.set(cmb_values[0])
    cmb.grid(row=6, column=1)
    # edit form(checkbuttons)
    checkbuttons = []
    for language in languagesv:
        ckb = IntVar()
        cb = Checkbutton(win, text=language, variable=ckb)
        cb.var = ckb
        checkbuttons.append(cb)
    for i, cb in enumerate(checkbuttons):
        cb['state'] = 'disabled'
        cb.grid(row=8+i, column=0)
    # edit form(methods)

    def search_employee(idd, fname, lname, pnum, address, rd):
        with open('List_of_employees.txt', 'r') as file:
            data = file.readlines()
        search_id = idd.get()
        employee_data = []
        found = False
        for i, line in enumerate(data):
            if line.startswith(f'id: {search_id}'):
                found = True
                employee_data = data[i:i + 8]
                break
        if found:
            try:
                fname.set(employee_data[1].split(':')[1].strip())
                lname.set(employee_data[2].split(':')[1].strip())
                pnum.set(employee_data[4].split(':')[1].strip())
                address.set(employee_data[5].split(':')[1].strip())
                fname_entry.delete(0, 'end')
                fname_entry.insert(0, fname.get())
                lname_entry.delete(0, 'end')
                lname_entry.insert(0, lname.get())
                pnum_entry.delete(0, 'end')
                pnum_entry.insert(0, pnum.get())
                address_entry.delete(0, 'end')
                address_entry.insert(0, address.get())
                if employee_data[3].split(":")[1].strip().endswith('Male'):
                    rd_male_radiobutton['value'] = rd.get()
                elif employee_data[3].split(":")[1].strip().endswith('Female'):
                    rd_female_radiobutton['value'] = rd.get()
                line = employee_data[6]
                if 'Salary: ' in line:
                    salary_value = line.split('Salary: ')[1].strip()
                    if salary_value in cmb_values:
                        cmb.set(salary_value)
                selected_languages = []
                languages = eval(employee_data[7].split('Language:')[1])
                for lang in languages:
                    if lang in languagesv:
                        selected_languages.append(lang)
                for cb in checkbuttons:
                    cb.var.set(1 if cb.cget('text') in selected_languages else 0)
                disable_enable_widgets(state='normal')
                cmb['state'] = 'readonly'
                id_entry['state'] = 'disabled'
                b1['state'] = 'disabled'
                for i, cb in enumerate(checkbuttons):
                    cb['state'] = 'normal'
            except Exception as e:
                messagebox.showerror('Error', str(e))
        else:
            messagebox.showinfo('Employee Not Found', f'No employee found with ID {search_id}')

    def update_employee(idd, fname, lname, pnum, address, rd, checkbuttons):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to update the employee data?')
        if response:
            with open('List_of_employees.txt', 'r') as file:
                data = file.readlines()
            search_id = idd.get()
            updated_data = []
            employee_found = False
            delete_data = False
            for line in data:
                if line.startswith(f'id: {search_id}'):
                    employee_found = True
                    delete_data = True
                    updated_data.extend([
                        f'id: {search_id}\n',
                        f'Name: {fname.get()}\n',
                        f'Last name: {lname.get()}\n',
                        f'Gender: {rd.get()}\n',
                        f'Telephone: {pnum.get()}\n',
                        f'Address: {address.get()}\n',
                        f'Salary: {cmb.get()}\n',
                    ])
                    formatted_languages = []
                    try:
                        for cb in checkbuttons:
                            if cb.cget('text') == 'Persian':
                                formatted_languages.append(f'\'{cb.cget('text')}\', ')
                            elif cb.cget('text') == 'English':
                                formatted_languages.append(f'\'{cb.cget('text')}\', ')
                            elif cb.cget('text') == 'Turkish':
                                formatted_languages.append(f'\'{cb.cget('text')}\')\n')
                            else:
                                formatted_languages.append(f'\' \', ')
                        updated_data.extend(f'Language: ({''.join(formatted_languages)})')
                    except Exception as e:
                        messagebox.showerror('Error', str(e))
                elif delete_data and line.startswith('Language: '):
                    delete_data = False
                elif not delete_data:
                    updated_data.append(line)
            if not employee_found:
                messagebox.showinfo('Employee Not Found', f'No employee found with Id: {search_id}')
                return
            with open('List_of_employees.txt', 'w') as file:
                file.writelines(updated_data)
            messagebox.showinfo('Update Successful', 'Employee data updated successfully')
            disable_enable_widgets(state='disabled')

    def disable_enable_widgets(state):
        widgets_to_disable_enable = [
            fname_entry,
            lname_entry,
            pnum_entry,
            address_entry,
            rd_male_radiobutton,
            rd_female_radiobutton,
            b2
        ]
        for widget in widgets_to_disable_enable:
            widget['state'] = state
    win.mainloop()


def search():
    # design for search form
    win = Toplevel()
    win.title('Search employees')
    win.geometry('300x570')
    win.resizable(False, True)
    win.config()
    win.iconbitmap('document.ico')
    with open('List_of_employees.txt', 'r') as file:
        r = file.read()
    # search form(Entries)
    idd = Entry(win)
    idd.place(x=90, y=20)
    # search form(labels)
    Label(win, text='Enter the ID:').place(x=20, y=20)
    lb = Label(win, text=r)
    lb.place(x=40, y=60)
    # search form(method)

    def search_employ():
        try:
            e = idd.get()
            with open('List_of_employees.txt', 'r') as f:
                lines = f.readlines()
                found = False
                for i, line in enumerate(lines):
                    if e in line:
                        found = True
                        employee_info = ''.join(lines[i:i+8])
                        Label(win, text=f'Employee Info: \n{employee_info}').place(x=40, y=70)
                        lb.destroy()
                        SYN_WES.success()
                        break
                if not found:
                    messagebox.showinfo('Info', 'Employee not found')
        except Exception as e:
            messagebox.showerror('Error', str(e))
    # search form(Button)
    Button(win, text='OK', command=search_employ).place(x=220, y=20)
    win.mainloop()
