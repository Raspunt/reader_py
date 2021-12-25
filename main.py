from app_obj import app_Objects
from book_db import books_db



db = books_db()

# db.create_table()

# db.insert_book("Не видя звёзд",
# "Вадим Панов",'1993',
# "научная_фантастика","books/не_видя_звезд.fb2")

# db.insert_book("Семь дней до Мегиддо",
# "Сергей Лукьяненко",'2021',
# "научная_фантастика","books/Семь_дней_до_Мегиддо.fb2")

# db.insert_book("Конёк-горбунок",
# "Пётр Ершов",'1834',
# "стихи_и_поэзия","books/Конек-Горбунок.epub")

# db.insert_book("Шестой дозор",
# "Сергей Лукьяненко",'2016',
# "книги_про_вампиров","books/шестой_дозор.fb2")




a = app_Objects()
a.start()


