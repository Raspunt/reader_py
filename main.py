import tkinter as tk
from  tkinter import ttk
from book_db import books_db  
from tkinter import * 

db = books_db()
root = tk.Tk()
root.geometry("500x500")

books_grid = ttk.Treeview(root)


books_grid['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

books_grid.column("#0", width=0,  stretch=NO)
books_grid.column("player_id",anchor=CENTER, width=80)
books_grid.column("player_name",anchor=CENTER,width=80)
books_grid.column("player_Rank",anchor=CENTER,width=80)
books_grid.column("player_states",anchor=CENTER,width=80)
books_grid.column("player_city",anchor=CENTER,width=80)

books_grid.heading("#0",text="",anchor=CENTER)
books_grid.heading("player_id",text="Id",anchor=CENTER)
books_grid.heading("player_name",text="название книги",anchor=CENTER)
books_grid.heading("player_Rank",text="автор",anchor=CENTER)
books_grid.heading("player_states",text="год издания",anchor=CENTER)
books_grid.heading("player_city",text="Жанр",anchor=CENTER)



count =0
for book in db.get_all_column():
    books_grid.insert(parent='',index='end',iid=count,text='',
    values=book)
    count = count + 1

books_grid.pack()

message = tk.Label(root, text="Жанры")
message.pack(side=LEFT)

n = tk.StringVar()
selectBox = ttk.Combobox(root, width = 27, textvariable = n)
  
# Adding combobox drop down list
selectBox['values'] = (db.get_all_genres())

selectBox.pack(side=LEFT)


root.mainloop()