import tkinter as tk
from tkinter import ttk,messagebox
import databasebackend as db


mainWindow = tk.Tk()
mainWindow.title('Student Management System')
mainWindow.geometry('600x500')

heading = tk.Label(mainWindow, text='Student Management System',font=("Helvetica 12",20))
heading.grid(row=0,columnspan=2,padx=10,pady=10)

nameLabel = tk.Label(mainWindow, text="Name").grid(row=1, column=0, padx=(10,20),pady=(30,20))
collegeLabel = tk.Label(mainWindow, text="College").grid(row=2, column=0, padx=(10,10))
phoneLabel = tk.Label(mainWindow, text="Phone Number").grid(row=3, column=0, padx=10)
addressLabel = tk.Label(mainWindow, text="Address").grid(row=4, column=0, padx=10)

student_name_entry = tk.Entry(mainWindow)
college_entry = tk.Entry(mainWindow)
phone_entry = tk.Entry(mainWindow)
address_entry = tk.Entry(mainWindow)

student_name_entry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
college_entry.grid(row=2, column=1, padx=(0,10), pady = 20)
phone_entry.grid(row=3, column=1, padx=(0,10), pady = 20)
address_entry.grid(row=4, column=1, padx=(0,10), pady = 20)

def takeValueInput():
    name = student_name_entry.get()
    student_name_entry.delete(0, tk.END)
    college = college_entry.get()
    college_entry.delete(0, tk.END)
    address = address_entry.get()
    address_entry.delete(0, tk.END)
    phone = int(phone_entry.get())
    phone_entry.delete(0, tk.END)

    if db.insert(name, college, address, str(phone)):
        messagebox.showinfo("Saved","Data Saved Successfully")
    else:
        messagebox.showerror("error","Data Not Saved")


save_button = tk.Button(mainWindow, text='Save Record',command = lambda : takeValueInput())
save_button.grid(row=5,column=0)

display_button = tk.Button(mainWindow, text='Display Record',command = lambda: displaywindow())
display_button.grid(row=5,column=1)


def displaywindow():
    mainWindow.destroy()
    displayWin = tk.Tk()

    displayWin.title("Display results")

    label = tk.Label(displayWin, text="Student Management System")
    label.pack()

    tree = ttk.Treeview(displayWin)
    tree["columns"] = ("first", "second", "third", "fourth")

    tree.heading("first", text="Student Name")
    tree.heading("second", text="College Name")
    tree.heading("third", text="Address")
    tree.heading("fourth", text="Phone Number")

    cursor = db.display()
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    displayWin.mainloop()


mainWindow.mainloop()
