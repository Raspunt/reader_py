import tkinter as tk
from  tkinter import ttk
from tkinter import * 
from book_db import books_db 
import os 









class Application:

    db = books_db()
    root = tk.Tk()
    root.geometry("670x300")



    def set_book_grid(self,books_grid):
        self.books_grid = books_grid

    def set_filterBtn(self,filterBtn):
        self.filterBtn = filterBtn


    def CreateTable(self,data_db:list):

        self.books_grid['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
        self.books_grid.column("#0", width=0,  stretch=NO)
        self.books_grid.column("player_id",anchor=CENTER, width=30)
        self.books_grid.column("player_name",anchor=CENTER,width=150)
        self.books_grid.column("player_Rank",anchor=CENTER,width=150)
        self.books_grid.column("player_states",anchor=CENTER,width=150)
        self.books_grid.column("player_city",anchor=CENTER,width=150)
        self.books_grid.heading("#0",text="",anchor=CENTER)
        self.books_grid.heading("player_id",text="Id",anchor=CENTER)
        self.books_grid.heading("player_name",text="название книги",anchor=CENTER)
        self.books_grid.heading("player_Rank",text="автор",anchor=CENTER)
        self.books_grid.heading("player_states",text="год издания",anchor=CENTER)
        self.books_grid.heading("player_city",text="Жанр",anchor=CENTER)



        count =0
        for book in data_db:
            self.books_grid.insert(parent='',index='end',iid=count,text='',
            values=book)
            count = count + 1

        self.books_grid.pack()


 
    # фильтровать по дате

    filter_status = 1
    def buttonFilter(self):


        if self.filter_status == 1:
            collum = self.db.filter_by_year_DESC()
            self.ClearTable()
            self.CreateTable(collum)
            self.filter_status = 2

            self.filterBtn.config(text="год издания по возростанию")



        
        elif self.filter_status == 2:
            collum = self.db.filter_by_year_ASC()
            self.ClearTable()
            self.CreateTable(collum)
            self.filter_status = 3
            
            self.filterBtn.config(text="год издания по убыванию")



        
        elif self.filter_status == 3:
            collum = self.db.get_all_column()
            self.ClearTable()
            self.CreateTable(collum)
            self.filter_status = 1

            self.filterBtn.config(text="без фильтров")


    def OpenBtn(self):
        
        path_books = self.db.get_all_path_book()
        cur_book =  self.books_grid.focus()

        int_cur_book = int(cur_book)
        book = str(path_books[int_cur_book])        
        book = book.replace(")","").replace("(","").replace("'","").replace(",","")



        os.system("fbreader " + book)
     



    def ClearTable(self):
        for i in self.books_grid.get_children():
            self.books_grid.delete(i)

        


    