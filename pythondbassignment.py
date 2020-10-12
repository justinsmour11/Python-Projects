
import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


        

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()

conn.close()

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    for fname in fileList:
        if fname.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (fname,))
            print(fname)

    conn.commit()
conn.close()
