import tkinter as tk
from  tkinter import ttk
from tkinter import * 
from app import Application
from book_db import books_db

class app_Objects:

    app = Application()
    db = books_db()

    root = app.root

    n = tk.StringVar() # тип комбо бокса cвязан с переменной selectBox 

    #  обьекты на форме
    books_grid = ttk.Treeview(root)
    label1 = tk.Label(root, text="Жанры")
    selectBox = ttk.Combobox(root, width = 27, textvariable = n)
    filterBtn = tk.Button(root, text ="Фильтр", command = app.buttonFilter)
    resetBtn = tk.Button(root, text ="Сбросить", command = app.buttonFilter)
    appendBtn = tk.Button(root, text ="Открыть", command = app.OpenBtn)



    
    app.set_book_grid(books_grid)
    app.set_filterBtn(filterBtn)

    def start(self):

        self.app.CreateTable(self.db.get_all_column())

        self.selectBox['values'] = (self.db.get_all_genres())
        
        
     
        self.label1.pack(side=LEFT)
        self.selectBox.pack(side=LEFT)
        self.filterBtn.pack(side=LEFT)
        self.resetBtn.pack(side=LEFT)
        self.appendBtn.pack(side=LEFT)

        self.books_grid.pack(side=TOP, anchor=NW)

        





        self.root.mainloop()

