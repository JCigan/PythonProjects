import os
import wx
import shutil
import datetime

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File Transfer Automation GUI")
        panel = wx.Panel(self, wx.ID_ANY)

        self.currentDirectory = os.getcwd()

        self.source = 'C:\Users\Student\Desktop\AllFiles'
        self.destination = 'C:\Users\Student\Desktop\RecentFiles'

        sourceDirBtn = wx.Button(panel, label="Choose source directory:")
        sourceDirBtn.Bind(wx.EVT_BUTTON, self.onSource)

        destDirBtn = wx.Button(panel, label="Choose destination directory:")
        destDirBtn.Bind(wx.EVT_BUTTON, self.onDest)

        operationBtn = wx.Button(panel, label="File Transfer")
        operationBtn.Bind(wx.EVT_BUTTON, self.onOperation)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(sourceDirBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(destDirBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(operationBtn, 0, wx.ALL|wx.CENTER, 5)
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
            print "You chose %s" % self.source
        dlg.Destroy()

    def onDest(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.destination = dlg.GetPath()
            print "You chose %s" % self.destination
        dlg.Destroy()

    def onOperation(self, event):
        source_files = os.listdir(self.source)
        for files in source_files:
            t = os.path.getmtime(self.source + '\\' + files)
            modification_date = datetime.datetime.fromtimestamp(t)
            if modification_date + datetime.timedelta(1) >= datetime.datetime.now():
                shutil.copyfile(self.source + '\\' + files, self.destination + '\\' + files)
                print 'Moved file: ' + self.source + '\\' + files


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
