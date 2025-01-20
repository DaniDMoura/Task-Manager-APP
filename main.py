from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser 
import os

saves_dir = "Saves"
if not os.path.exists(saves_dir):
    os.makedirs(saves_dir)



def add():
    #Validation
    new = entry.get()
    if new == '':
        messagebox.showerror(title ='Error', message='Empty input, enter your task')
    else:
        #Commands
        def cancel(new_window):
            new_window.destroy()
            entry.delete(0,END)

        def ok(new_window,status,new):
            status_value = status.get()
            if status_value == 0:
                show_tasks.insert(END, f'{new}, Not Done')
            elif status_value == 1:
                show_tasks.insert(END, f'{new}, In-Progress')
            elif status_value == 2:
                show_tasks.insert(END, f'{new}, Done')
            new_window.destroy()
            entry.delete(0,END)


        #New Window Configure
        new_window = Toplevel()
        new_window.title("Add Task")
        new_window.geometry('200x220')
        new_window.resizable(False, False)
        
        Label(new_window, text="Select task status:").pack(anchor=W,pady=10)

        status = IntVar()
        status.set(0)
        status_options = ["Not Done", "In-Progress", "Done"]

        for index in range(len(status_options)):
            Radiobutton(new_window,
                        text=status_options[index],
                        variable=status,
                        value=index,
                        width = 20,
                        command=lambda: ok(new_window,status,new),
                        ).pack(side=TOP, pady=5)
            
        button_frame = Frame(new_window)
        button_frame.pack(pady=20)

        button_cancel = Button(button_frame, text="Cancel", width=10,command=lambda: cancel(new_window))
        button_cancel.pack(side=TOP, padx=5, pady=5)          

def delete():
    for index in reversed(show_tasks.curselection()):
        show_tasks.delete(index)

def delete_all():
    if messagebox. askyesno( title='Delete All' , message='Do you want to proceed?'):
        show_tasks.delete(0, END)

def save():
    file = filedialog.asksaveasfilename(initialdir=saves_dir,
                                    defaultextension='.txt',
                                    filetypes=[('Text file','.txt'),
                                                ('All files','.*')])
    try:
        if file:
            with open(file, "w") as file:
                for item in show_tasks.get(0,END):
                    file.write(item + "\n")
    except Exception as e:
        print(f"Error caused by: {e}")

def load():
    file_loaded = filedialog.askopenfilename(initialdir=saves_dir,
                                           title="Open file",
                                           filetypes=[("text files","*.txt"),("all files","*.*")])
    if file_loaded:
        with open(file_loaded,'r') as file_loaded:
            for item in file_loaded:
                show_tasks.insert(END, item.strip())

def exit():
    window.destroy()


window = Tk()
icon = PhotoImage(file="Icon/task-management-8.png")
window.iconphoto(True, icon)
window.title("Task Tracker")
window.geometry("275x320")
window.resizable(False, False)
window.config(bg="#E0E0E0")

style = Style()
style.theme_use("clam")

entry = Entry(window,width=45)

button_add = Button(window, text="Add",width=10,
                        command=add)
button_delete = Button(window, text="Delete", width=10,
                        command=delete)
button_delete_all = Button(window, text="Delete All", width=10,
                        command=delete_all)
show_tasks = Listbox(window, height=10, width=45)
button_save = Button(window, text="Save", width=10,
                        command=save)
button_load = Button(window, text="Load", width=10,
                        command=load)
button_exit = Button(window, text="Exit", width=10,
                        command=exit)





entry.grid(row=0, column=0, columnspan=3, pady=10)
button_add.grid(row=1, column=0, padx=5, pady=5)
button_delete.grid(row=1, column=1, padx=5, pady=5)
button_delete_all.grid(row=1, column=2, padx=5, pady=5)
show_tasks.grid(row=2, column=0, columnspan=3, pady=10)
button_save.grid(row=3, column=0, padx=5, pady=10)
button_load.grid(row=3, column=2, padx=5, pady=10)
button_exit.grid(row=3, column=1, padx=5, pady=10)


window.mainloop()    