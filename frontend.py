import tkinter as tk
import backend

def view_command() :
	list1.delete(0, tk.END)
	for row in backend.view_data():
		list1.insert(tk.END, row)

def search_command() :
	list1.delete(0, tk.END)
	for row in backend.search_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) :
		list1.insert(tk.END, row)

def add_command() :
	backend.insert_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) 
	list1.delete(0, tk.END)
	list1.insert(tk.END, "Succesfully inserted: ")
	list1.insert(tk.END, backend.view_data()[-1])

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,tk.END)
        e1.insert(tk.END,selected_tuple[1])
        e2.delete(0,tk.END)
        e2.insert(tk.END,selected_tuple[2])
        e3.delete(0,tk.END)
        e3.insert(tk.END,selected_tuple[3])
        e4.delete(0,tk.END)
        e4.insert(tk.END,selected_tuple[4])
    except IndexError:
        pass

def delete_command() :
	backend.delete_data(selected_tuple[0])
	list1.delete(0, tk.END)
	list1.insert(tk.END, "Succesfully deleted ")
	list1.insert(tk.END, selected_tuple)
    
def update_command() :
	backend.update_data(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	list1.delete(0, tk.END)
	list1.insert(tk.END, "Succesfully updated to: ")
	list1.insert(tk.END, (selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

window = tk.Tk()

l1 = tk.Label(window, text="Title")
l1.grid(row=0, column=0)

title_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

l2 = tk.Label(window, text="Author")
l2.grid(row=0, column=2)

author_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

l1 = tk.Label(window, text="Year")
l1.grid(row=1, column=0)

year_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

l4 = tk.Label(window, text="ISBN")
l4.grid(row=1, column=2)

isbn_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

b1 = tk.Button(window, text="View All", command=view_command)
b1.grid(row=2, column=3)
b1.config(width=20)

b2 = tk.Button(window, text="Search Entry", command=search_command)
b2.grid(row=3, column=3)
b2.config(width=20)

b3 = tk.Button(window, text="Add Entry", command=add_command)
b3.grid(row=4, column=3)
b3.config(width=20)

b1 = tk.Button(window, text="Update Selected", command=update_command)
b1.grid(row=5, column=3)
b1.config(width=20)

b1 = tk.Button(window, text="Delete Selected", command=delete_command)
b1.grid(row=6, column=3)
b1.config(width=20)

b1 = tk.Button(window, text="Close", command=window.destroy)
b1.grid(row=7, column=3)
b1.config(width=20)

list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()
