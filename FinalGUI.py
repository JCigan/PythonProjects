import wx
import sqlite3
import os
import shutil
import datetime
import time

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE IF NOT EXISTS fileTransfer(\
transferTime Datetime)")
    conn.commit()

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File Transfer Automation GUI")
        panel = wx.Panel(self, wx.ID_ANY)
        
        self.currentDirectory = os.getcwd()




        sizer = wx.BoxSizer(wx.VERTICAL)


        self.source = 'C:\Users\Student\Desktop\AllFiles'
        self.destination = 'C:\Users\Student\Desktop\RecentFiles'

        sourceDirBtn = wx.Button(panel, label="Choose source directory:")
        sourceDirBtn.Bind(wx.EVT_BUTTON, self.onSource)

        destDirBtn = wx.Button(panel, label="Choose destination directory:")
        destDirBtn.Bind(wx.EVT_BUTTON, self.onDest)

        operationBtn = wx.Button(panel, label="File Transfer")
        operationBtn.Bind(wx.EVT_BUTTON, self.onOperation)

        sql = "SELECT transferTime FROM fileTransfer ORDER BY transfertime DESC\
 LIMIT 1"
        for row in c.execute(sql):
            self.last_time = str(row).replace('(', '').replace('u\'', '').\
                             replace("',", "").replace(')', '')

        self.textBox = wx.StaticText(panel, -1, label = "Time of Last Transfer: \
%s" % self.last_time)

        self.dialogBox = wx.StaticText(panel, -1, label = "")

        sizer.Add(sourceDirBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(destDirBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(operationBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.textBox, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.dialogBox, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)



    def onSource(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.source = dlg.GetPath()
            self.DialogBox.SetLabel("You chose %s" % self.source)
        dlg.Destroy()

    def onDest(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.destination = dlg.GetPath()
            self.DialogBox.SetLabel("You chose %s" % self.destination)
        dlg.Destroy()

    def onOperation(self, event):
        source_files = os.listdir(self.source)
        for files in source_files:
            t = os.path.getmtime(self.source + '\\' + files)
            modification_date = str(datetime.datetime.fromtimestamp(t))
            if type(self.last_time) == None or modification_date > self.last_time:
                shutil.copyfile(self.source + '\\' + files, self.destination + '\\' + files)
                self.DialogBox.SetLabel('Moved file: ' + self.source + '\\' + files)
                time.sleep(1000)
        self.transfer_time = (datetime.datetime.fromtimestamp\
        (int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
        self.last_time = self.transfer_time
        c.execute("INSERT INTO fileTransfer (transferTime) VALUES(?)", (self.transfer_time,))
        conn.commit()
        self.textBox.SetLabel("Time of Last Transfer: \
%s" % self.last_time)


if __name__ == "__main__":
    tableCreate()
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
