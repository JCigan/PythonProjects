from tkinter import *
from tkinter import ttk


class Feedback:

    def __init__(self, master):

        master.title('Create Your Own Website')

        self.style = ttk.Style()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        self.text = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        self.text.grid(row = 3, column = 0)
        ttk.Button(self.frame_content, text = 'Create Web Page', command = self.submit).grid(row=1, column=0)


    def submit(self):

        bodyText = self.text.get(1.0, 'end')
        web_page = '''<!DOCTYPE html
<html>
<body>
{0}
</body>
</html>'''.format(bodyText)
        output = open("yourWebPage.html", "w")
        output.write(web_page)
        output.close()



def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()

# label = ttk.Label(root, text = "Hello, Tkinter!")
