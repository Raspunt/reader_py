import tkinter as tk
from  tkinter import ttk
from tkinter import * 
from book_db import books_db 
from tkinter import filedialog as fd
from create_window import CreateWindow

import os 


class Application:

    db = books_db()
    root = tk.Tk()
    root.geometry("870x300")



    def set_book_grid(self,books_grid):
        self.books_grid = books_grid

    def set_filterBtn(self,filterBtn):
        self.filterBtn = filterBtn
    
    def set_ComboBox(self,comboBox):
        self.comboBox = comboBox

    def set_infoLabel2(self,infoLabel2):
        self.infoLabel2 = infoLabel2
    



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


        cmd = "start "+book
        os.system("taskkill /IM FBReader.exe" )
        os.system(cmd)
     



    def ClearTable(self):
        for i in self.books_grid.get_children():
            self.books_grid.delete(i)

    
    def ComboBoxOnChange(self,data):
        
        self.ClearTable()

        genre_name = self.comboBox.get()
        # print(genre_name)
        genre_name = str(genre_name.replace("{","").replace("}",""))

        content = self.db.get_all_column()
        
        sort_arr = []
        for con in content:
            genre = str(con[4])
            if genre == str(genre_name):
                sort_arr.append(content[con[0] -1])

              
        self.CreateTable(sort_arr)


    def resetBtn(self):
        self.ClearTable()
        self.CreateTable(self.db.get_all_column())


    def ingo_update(self,data):
        
        file_id = self.books_grid.focus()
        int_file_id = int(file_id)
        files_path = self.db.get_all_path_book()

        file_path = files_path[int_file_id]

        file_path = str(file_path).replace("'","").replace(",","").replace("(","").replace(")","")

        try:
            

            for line in self.read_first_20_lines(file_path):

                line = str(line).replace("<annotation>","").replace("<p>","").replace("</p>","")
                line = str(line).replace("\n","")

                self.infoLabel2.delete(1.0,END)
                self.infoLabel2.insert(tk.END,line)
                
        



        except UnicodeDecodeError as e:
            print("информация не получена")

            




     
    def read_first_20_lines(self,file_path:str):

        isAnotation = False
        lines = []

        with open(file_path,'r', encoding='utf8') as f:
            
            for i in range(1,25):
                line = f.readline()

                if line.find("<annotation>") != -1:
                    isAnotation = True
                
                if line.find("</annotation>") != -1:
                    isAnotation = False
                
                if isAnotation == True:
                    lines.append(line)

            f.close()

       
        
  

        return lines


   
    def CreateBook(self):

        # cw = CreateWindow()
        # cw.start(self.root)
        window = Toplevel(self.root)
        window.geometry("600x300")


        label_title = Label(window, text = "Название книги")
        input_title = Entry(window, bd = 5,width=50)
        label_author = Label(window, text = "автор")
        input_author = Entry(window, bd = 5,width=50)
        label_year = Label(window, text = "год издания")
        input_year = Entry(window, bd = 5,width=50)
        label_genre = Label(window, text = "Жанр")
        input_genre = Entry(window, bd = 5,width=50)
        label_path_book = Label(window, text = "путь к книге")
        input_path_book = Entry(window, bd = 5,width=50)

        def GetPathToBook():
            filename = fd.askopenfilename()
            input_path_book.insert(0,filename)
    
            


        load_btn = tk.Button(window, text ="Открыть", command = GetPathToBook)





            
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

    
     
        


        



    
