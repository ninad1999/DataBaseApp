"""
	This app stores information of books:
		Title, Author, Year, ISBN

	User can:
		View all records
		Search an entry
		Add an entry
		Update an entry
		Delete an entry
		Exit App

"""

import tkinter as tk

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

b1 = tk.Button(window, text="View All")
b1.grid(row=2, column=3)
b1.config(width=20)

b2 = tk.Button(window, text="Search Entry")
b2.grid(row=3, column=3)
b2.config(width=20)

b3 = tk.Button(window, text="Add Entry")
b3.grid(row=4, column=3)
b3.config(width=20)

b1 = tk.Button(window, text="Update Entry")
b1.grid(row=5, column=3)
b1.config(width=20)

b1 = tk.Button(window, text="Delete Entry")
b1.grid(row=6, column=3)
b1.config(width=20)

b1 = tk.Button(window, text="Close")
b1.grid(row=7, column=3)
b1.config(width=20)

list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()
