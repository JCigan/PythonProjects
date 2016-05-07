from tkinter import *
from tkinter import ttk
import sqlite3 as sqlite

conn = sqlite.connect('tutorial.db')
c = conn.cursor()

def createdb():
    c.execute("CREATE TABLE IF NOT EXISTS StoredStrings(TextString varchar(500))")

class Feedback:

    def __init__(self, master):

        master.title('Create Your Own Website')

        self.style = ttk.Style()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        self.text = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        self.text.grid(row = 3, column = 0)
        ttk.Button(self.frame_content, text = 'Create From Text Box', command = self.submit).grid(row=1, column=0)
        ttk.Button(self.frame_content, text = 'Create From Database', command = self.submitdb).grid(row=1, column=1)
        ttk.Button(self.frame_content, text = 'Store Text', command = self.storedb).grid(row=2, column=0)
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row=2, column=1)


        self.db_list = Listbox(master)
        self.db_list.pack()
        sql = "SELECT TextString FROM StoredStrings"
        for row in c.execute(sql):
            self.db_list.insert(END, str(row).replace("('", '').replace("\\n',)", ''))

    def submit(self):

        self.submission = self.text.get(1.0, 'end')
        web_page = '''<!DOCTYPE html
<html>
<body>
{0}
</body>
</html>'''.format(self.submission)
        output = open("yourWebPage.html", "w")
        output.write(web_page)
        output.close()

    def clear(self):

        self.text.delete(0.0, 'end')

    def submitdb(self):

        self.selection = self.db_list.curselection()
        self.submission = self.db_list.get(self.selection)
        web_page = '''<!DOCTYPE html
<html>
<body>
{0}
</body>
</html>'''.format(self.submission)
        output = open("yourWebPage.html", "w")
        output.write(web_page)
        output.close()

    def storedb(self):

        insert_text = self.text.get(1.0, 'end')
        c.execute("INSERT INTO StoredStrings (TextString) VALUES(?)", (insert_text,))
        conn.commit()
        self.db_list.insert(END, insert_text)
        self.text.delete(0.0, 'end')






def main():

    createdb()
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
