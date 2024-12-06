import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not exists book(id integer primary key,title text,author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("insert into book values(null,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("delete from book where id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("update book set (title=?, author=?, year=?, isbn=?) where id =?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()

# insert("The Wizard of Oz", "L. Frank Baum", "1900", "9780517500866")
# insert("Shadow and Bone", "Leigh Bardugo", "2012", "9780805094596")
# insert("Charlie and the Chocolate Factory", "Roald Dahl", "1964", "9780060510657")
# insert("Charlotte's Web", "E. B. White", "1952", "9780807208526")
# insert("The Lion, the Witch and the Wardrobe", "C. S. Lewis", "1950", "9780001831803")
# insert("Lindsey Jones", "Basic Certificate", "2025","jonesl")


# print(view())