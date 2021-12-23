import sqlite3



class books_db:

    conn = sqlite3.connect("books.db")
    c = conn.cursor()

    # title
    # author
    # year
    # path_img
    # genre

    def create_table(self):
        self.c.execute(f"""CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT ,
            title text NOT NULL,
            author text NOT NULL,
            year text NOT NULL,
            genre text NOT NULL,
            path_book text NOT NULL
            )""")
        self.conn.commit()



    def insert_book(self,title:str,author:str,year:str,genre:str,path_book:str,):
        self.c.execute(f"""INSERT  INTO books(title,author,year,genre,path_book) VALUES ( 
        '{title}',
        '{author}',
        '{year}',
        '{genre}',
        '{path_book}'
        )
        """)
        self.conn.commit()

    def get_all_column(self):
        colloum_arr = []
        self.c.execute("SELECT  * FROM  books")

        rows = self.c.fetchall()
        for row in rows:
            colloum_arr.append(row)
        
        return colloum_arr

    def filter_by_year_DESC(self):
        colloum_arr = []
        self.c.execute(f"SELECT * FROM books ORDER BY year DESC")

        rows = self.c.fetchall()
        for row in rows:
            colloum_arr.append(row)
        
        return colloum_arr

    def filter_by_year_ASC(self):
        colloum_arr = []
        self.c.execute(f"SELECT * FROM books ORDER BY year ASC")

        rows = self.c.fetchall()
        for row in rows:
            colloum_arr.append(row)

        return colloum_arr
    
    def get_all_genres(self):
        colloum_arr = []
        self.c.execute(f"SELECT genre FROM books ")

        rows = self.c.fetchall()
        for row in rows:
            if row not in colloum_arr:
                colloum_arr.append(row)
        
        return colloum_arr


    def get_all_path_book(self):
        colloum_arr = []
        self.c.execute(f"SELECT path_book FROM books ")

        rows = self.c.fetchall()
        for row in rows:
            colloum_arr.append(row)

        return colloum_arr


    def close_db(self):
        self.conn.close()

# create_table()
# insert_book("Конец Вечности","Айзек азимов",1955,"фантастика")
# insert_book("Конец Вечности","Айзек азимов",1925,"фантастика")
# insert_book("Конец Вечности","Айзек азимов",1900,"фантастика")
# get_all_values()


# filter_by_year_DESC()
# print("\n")
# filter_by_year_ASC()

