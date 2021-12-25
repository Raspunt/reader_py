import tkinter as tk
from  tkinter import ttk
from tkinter import * 
from book_db import books_db 
from tkinter import filedialog as fd

import os 

class CreateWindow:
    
    def GetPathToBook(self):
        filename = fd.askopenfilename()
        self.label_path_book.insert(0,filename)
    

    def start(self,root):
        window = Toplevel(root)
        window.geometry("300x300")


        label_title = Label(window, text = "Название книги")
        input_title = Entry(window, bd = 5)
        label_author = Label(window, text = "автор")
        input_author = Entry(window, bd = 5)
        label_year = Label(window, text = "год издания")
        input_year = Entry(window, bd = 5)
        label_genre = Label(window, text = "Жанр")
        input_genre = Entry(window, bd = 5)
        label_path_book = Label(window, text = "путь к книге")
        input_path_book = Entry(window, bd = 5)
        load_btn = tk.Button(window, text ="Открыть", command = self.GetPathToBook)


            
        label_title.grid(row=0,column=0)
        input_title.grid(row=0,column=1)

        label_author.grid(row=1,column=0)
        input_author.grid(row=1,column=1)

        label_year.grid(row=2,column=0)
        input_year.grid(row=2,column=1)

        label_genre.grid(row=3,column=0)
        input_genre.grid(row=3,column=1)

        label_path_book.grid(row=4,column=0)
        input_path_book.grid(row=4,column=1)
        load_btn.grid(row=4,column=2)
