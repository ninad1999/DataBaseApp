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
import sqlite3

def connect() :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	 conn.commit()
	 conn.close()

def insert_data(title, author, year, isbn) :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
	 conn.commit()
	 conn.close()
	
def view_data() :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("SELECT * FROM book")
	 rows = cur.fetchall()
	 conn.close()

	 return rows

def search_data(title="", author="", year="", isbn="") :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
	 rows = cur.fetchall()
	 conn.close()

	 return rows

def delete_data(id) :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("DELETE FROM book WHERE id=?", (id,))
	 conn.commit()
	 conn.close()
	
def update_data(id, title, author, year, isbn) :
	 conn = sqlite3.connect("books.db")
	 cur = conn.cursor()
	 cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
	 conn.commit()
	 conn.close()

connect()
