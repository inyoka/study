import sqlite3

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

con = sqlite3.connect('sqlite:///app.db')

data = ['Student One', '6 Ferndene Drive', '25/04/1977', 0, 0, 0, 0, 'Plumber',
        'Inactive', 0, '16:00', '12/19/1988', '23/08/1989',
        'Lost', 'Good grammar']


stmt = "INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?,\
                                    ?, ?, ?, ?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()
