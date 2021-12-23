from app_obj import app_Objects
from book_db import books_db

db = books_db()

# db.create_table()

# db.insert_book("Не видя звёзд",
# "Вадим Панов",'1993',
# "Cтимпанк","books/не_видя_звезд.fb2")


a = app_Objects()
a.start()


